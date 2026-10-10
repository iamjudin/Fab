import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "plugins/fab/skills/product/scripts/product_workspace.py"
SPEC = importlib.util.spec_from_file_location("product_workspace", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class ProductWorkspaceTests(unittest.TestCase):
    def test_canvas_links_use_actual_vault_not_nested_product_root(self):
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            product = vault / 'nested-product'
            (product / 'product').mkdir(parents=True)
            (product / 'product/note.md').write_text('Source')
            canvas = product / 'map.canvas'
            document = {'nodes': [{'id': 'source', 'type': 'file', 'file': 'product/note.md'}], 'edges': []}
            canvas.write_text(json.dumps(document))
            self.assertEqual(MODULE.validate_canvas(product, canvas), 0)
            self.assertEqual(MODULE.validate_canvas(product, canvas, vault), 1)
            document['nodes'][0]['file'] = 'nested-product/product/note.md'
            canvas.write_text(json.dumps(document))
            self.assertEqual(MODULE.validate_canvas(product, canvas, vault), 0)

    def test_init_creates_valid_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            self.assertTrue((root / ".wireframer/signals.json").exists())
            self.assertTrue((root / "product/journal.md").exists())
            project = json.loads((root / ".wireframer/project.json").read_text(encoding="utf-8"))
            self.assertEqual(project["activeStage"], "human-jobs")

    def test_new_graph_cannot_reduce_review_entities_to_ids_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            graph_path = root / ".wireframer/graph.json"
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
            self.assertEqual(graph["schemaVersion"], 2)
            graph["nodes"] = [
                {"id": "HJ-01", "type": "human-job", "status": "assumption", "links": []}
            ]
            graph_path.write_text(json.dumps(graph), encoding="utf-8")
            self.assertEqual(MODULE.validate_workspace(root), 1)

            graph["nodes"][0]["meaning"] = "Сохранять ясную договорённость о возврате"
            graph_path.write_text(json.dumps(graph), encoding="utf-8")
            self.assertEqual(MODULE.validate_workspace(root), 0)

    def test_validator_catches_dangling_graph_and_signal_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            MODULE.init_workspace(root, "sample", "ru")
            graph_path = root / ".wireframer/graph.json"
            signals_path = root / ".wireframer/signals.json"
            graph_path.write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "nodes": [
                            {
                                "id": "JS-01.1",
                                "type": "job-story",
                                "status": "assumption",
                                "links": ["HJ-99"],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            signals_path.write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "signals": [
                            {
                                "id": "SIG-01",
                                "meaning": "sample",
                                "authority": "direction",
                                "knowledgeStatus": "assumption",
                                "disposition": {
                                    "kind": "represented",
                                    "refs": ["HJ-99"],
                                },
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(MODULE.validate_workspace(root), 1)

    def test_capability_priority_classification_is_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            graph_path = root / ".wireframer/graph.json"
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
            graph["nodes"] = [
                {
                    "id": "CAP-01",
                    "type": "product-capability",
                    "meaning": "Open the approved material",
                    "status": "candidate",
                    "links": [],
                }
            ]
            graph_path.write_text(json.dumps(graph), encoding="utf-8")
            self.assertEqual(MODULE.validate_workspace(root), 1)

            graph["nodes"][0]["classification"] = "core"
            graph_path.write_text(json.dumps(graph), encoding="utf-8")
            self.assertEqual(MODULE.validate_workspace(root), 0)

    def test_impact_lists_direct_and_indirect_dependents_without_changing_graph(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            graph_path = root / ".wireframer/graph.json"
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
            graph["nodes"] = [
                {"id": "DR-01", "type": "domain-rule", "meaning": "Audio is original", "status": "decision", "links": []},
                {"id": "DR-02", "type": "domain-rule", "meaning": "Deletion policy", "status": "candidate", "links": ["DR-01"]},
                {"id": "CAP-01", "type": "product-capability", "meaning": "Recover deleted audio", "status": "candidate", "classification": "supporting", "links": ["DR-02"]},
                {"id": "DR-03", "type": "domain-rule", "meaning": "Unrelated access", "status": "candidate", "links": []},
            ]
            graph_path.write_text(json.dumps(graph), encoding="utf-8")
            before = graph_path.read_bytes()
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(MODULE.impact_report(root, "DR-01"), 0)
            report = json.loads(output.getvalue())
            self.assertEqual(report["changed"], "DR-01")
            self.assertEqual(
                [(item["id"], item["path"]) for item in report["affected"]],
                [("DR-02", ["DR-01", "DR-02"]), ("CAP-01", ["DR-01", "DR-02", "CAP-01"])],
            )
            self.assertEqual(graph_path.read_bytes(), before)

            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(MODULE.impact_report(root, "DR-03"), 0)
            self.assertEqual(json.loads(output.getvalue())["affected"], [])

    def test_signal_requires_one_meaning_and_one_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            signals_path = root / ".wireframer/signals.json"
            signals_path.write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "signals": [
                            {
                                "id": "SIG-01",
                                "meaning": " ",
                                "authority": ["direction", "hard-constraint"],
                                "knowledgeStatus": ["evidence", "assumption"],
                                "disposition": {"kind": ["represented", "routed"], "refs": []},
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(MODULE.validate_workspace(root), 1)

    def test_canvas_validator_checks_edges_and_vault_relative_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            source = root / "product/reviews/navigation-ia.md"
            source.write_text("# Navigation / IA\n", encoding="utf-8")
            canvas = root / "product/reviews/navigation-ia.canvas"
            content = {
                "nodes": [
                    {"id": "collection", "type": "text", "text": "Collection"},
                    {"id": "source", "type": "file", "file": "product/reviews/navigation-ia.md"},
                ],
                "edges": [
                    {"id": "link", "fromNode": "collection", "toNode": "source", "label": "IA"}
                ],
            }
            canvas.write_text(json.dumps(content), encoding="utf-8")
            self.assertEqual(MODULE.validate_canvas(root, canvas), 0)

            content["nodes"][1]["file"] = "product/reviews/missing.md"
            content["edges"][0]["toNode"] = "missing-node"
            canvas.write_text(json.dumps(content), encoding="utf-8")
            self.assertEqual(MODULE.validate_canvas(root, canvas), 1)

    def test_clean_removes_only_tracked_workspace_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "sample"
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            review = root / "product/reviews/human-jobs.md"
            review.write_text("# Human Jobs\n", encoding="utf-8")
            unrelated = root / "notes.txt"
            unrelated.write_text("keep me\n", encoding="utf-8")
            self.assertEqual(MODULE.track_files(root, [review]), 0)

            self.assertEqual(MODULE.clean_workspace(root, "sample"), 0)

            self.assertFalse(review.exists())
            self.assertFalse((root / ".wireframer").exists())
            self.assertTrue(unrelated.exists())

    def test_clean_rejects_wrong_slug(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "sample"
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            self.assertEqual(MODULE.clean_workspace(root, "different"), 1)
            self.assertTrue((root / ".wireframer/project.json").exists())

    def test_clean_rejects_path_escape_before_deleting_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "sample"
            outside = Path(directory) / "outside.txt"
            outside.write_text("keep me\n", encoding="utf-8")
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)
            manifest_path = root / ".wireframer/workspace.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["generatedFiles"].append("../outside.txt")
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            self.assertEqual(MODULE.validate_workspace(root), 1)
            self.assertEqual(MODULE.clean_workspace(root, "sample"), 1)

            self.assertTrue(outside.exists())
            self.assertTrue((root / ".wireframer/project.json").exists())

    def test_clean_removes_empty_container_created_for_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            container = Path(directory) / "Products"
            root = container / "sample"
            self.assertEqual(MODULE.init_workspace(root, "sample", "ru"), 0)

            self.assertEqual(MODULE.clean_workspace(root, "sample"), 0)

            self.assertFalse(container.exists())


if __name__ == "__main__":
    unittest.main()
