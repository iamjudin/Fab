#!/usr/bin/env python3
"""Initialize and structurally validate a Wireframer product workspace."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*-[0-9]+(?:\.[0-9]+)?$")
KNOWLEDGE_STATUSES = {"assumption", "evidence", "decision"}
DISPOSITIONS = {"represented", "routed", "deferred", "open-gap"}
WORKSPACE_MANIFEST = ".wireframer/workspace.json"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def init_workspace(root: Path, slug: str, language: str, active_stage: str = "human-jobs") -> int:
    root = root.resolve()
    state = root / ".wireframer"
    product = root / "product"
    missing_ancestors: list[Path] = []
    cursor = root
    while not cursor.exists() and cursor.parent != cursor:
        missing_ancestors.append(cursor)
        cursor = cursor.parent
    cleanup_boundary = cursor
    managed_directories = [root, state, product, product / "reviews", product / "evidence"]
    created_directories = list(
        dict.fromkeys(missing_ancestors + [path for path in managed_directories if not path.exists()])
    )
    (product / "reviews").mkdir(parents=True, exist_ok=True)
    (product / "evidence").mkdir(parents=True, exist_ok=True)
    state.mkdir(parents=True, exist_ok=True)

    files = {
        state / "project.json": {
            "schemaVersion": 1,
            "slug": slug,
            "language": language,
            "activeStage": active_stage,
        },
        state / "signals.json": {"schemaVersion": 1, "signals": []},
        state / "graph.json": {"schemaVersion": 2, "nodes": []},
    }
    created_files: list[Path] = []
    for path, value in files.items():
        if not path.exists():
            write_json(path, value)
            created_files.append(path)

    journal = product / "journal.md"
    if not journal.exists():
        journal.write_text(f"# Product Journal: {slug}\n", encoding="utf-8")
        created_files.append(journal)

    manifest_path = root / WORKSPACE_MANIFEST
    if not manifest_path.exists():
        write_json(
            manifest_path,
            {
                "schemaVersion": 1,
                "managedBy": "wireframer",
                "slug": slug,
                "cleanupBoundary": str(cleanup_boundary),
                "generatedFiles": [str(path.relative_to(root)) for path in created_files],
                "generatedDirectories": [
                    (
                        "."
                        if path == root
                        else str(path.relative_to(root))
                        if root in path.parents
                        else str(path)
                    )
                    for path in created_directories
                ],
            },
        )
    return validate_workspace(root)


def safe_relative_path(root: Path, value: str) -> Path:
    path = (root / value).resolve()
    if path != root and root not in path.parents:
        raise ValueError(f"path escapes workspace: {value}")
    return path


def safe_cleanup_directory(root: Path, boundary: Path, value: str) -> Path:
    raw_path = Path(value)
    path = raw_path.resolve() if raw_path.is_absolute() else (root / raw_path).resolve()
    if path == boundary or boundary not in path.parents:
        raise ValueError(f"cleanup directory crosses boundary: {value}")
    if path != root and root not in path.parents and path not in root.parents:
        raise ValueError(f"cleanup directory is unrelated to workspace: {value}")
    return path


def track_files(root: Path, paths: list[Path]) -> int:
    root = root.resolve()
    manifest_path = root / WORKSPACE_MANIFEST
    manifest = load_json(manifest_path, [])
    if manifest.get("managedBy") != "wireframer":
        print(f"ERROR: unmanaged workspace: {root}")
        return 1
    tracked = set(manifest.get("generatedFiles", []))
    for path in paths:
        resolved = path.resolve() if path.is_absolute() else (root / path).resolve()
        if resolved != root and root not in resolved.parents:
            print(f"ERROR: path escapes workspace: {path}")
            return 1
        if not resolved.is_file():
            print(f"ERROR: tracked path is not a file: {resolved}")
            return 1
        tracked.add(str(resolved.relative_to(root)))
    manifest["generatedFiles"] = sorted(tracked)
    write_json(manifest_path, manifest)
    return 0


def clean_workspace(root: Path, slug: str) -> int:
    root = root.resolve()
    manifest_path = root / WORKSPACE_MANIFEST
    errors: list[str] = []
    manifest = load_json(manifest_path, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if manifest.get("managedBy") != "wireframer" or manifest.get("slug") != slug:
        print("ERROR: workspace identity does not match cleanup request")
        return 1

    try:
        files = [safe_relative_path(root, value) for value in manifest.get("generatedFiles", [])]
        boundary = Path(manifest.get("cleanupBoundary", root)).resolve()
        directories = [
            safe_cleanup_directory(root, boundary, value)
            for value in manifest.get("generatedDirectories", [])
        ]
        for path in files:
            if path.is_file() or path.is_symlink():
                path.unlink()
        manifest_path.unlink(missing_ok=True)
    except (OSError, ValueError) as exc:
        print(f"ERROR: cleanup failed: {exc}")
        return 1

    for directory in sorted(directories, key=lambda path: len(path.parts), reverse=True):
        try:
            directory.rmdir()
        except OSError:
            pass
    print("Wireframer managed files: cleaned")
    return 0


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing file: {path}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"root must be an object: {path}")
        return {}
    return value


def validate_canvas(root: Path, canvas_path: Path, vault_root: Path | None = None) -> int:
    root = root.resolve()
    link_root = vault_root.resolve() if vault_root is not None else root
    if not root.is_relative_to(link_root):
        print("ERROR: product root must be inside the actual Obsidian vault root")
        return 1
    errors: list[str] = []
    try:
        path = safe_relative_path(root, str(canvas_path))
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1
    canvas = load_json(path, errors)
    nodes = canvas.get("nodes")
    edges = canvas.get("edges")
    if not isinstance(nodes, list):
        errors.append("canvas.nodes must be an array")
        nodes = []
    if not isinstance(edges, list):
        errors.append("canvas.edges must be an array")
        edges = []

    node_ids: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"canvas.nodes[{index}] must be an object")
            continue
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id:
            errors.append(f"canvas.nodes[{index}].id is required")
            continue
        if node_id in node_ids:
            errors.append(f"duplicate canvas node ID: {node_id}")
        node_ids.add(node_id)
        if node.get("type") == "file":
            file_path = node.get("file")
            if not isinstance(file_path, str) or not file_path:
                errors.append(f"{node_id}.file is required")
                continue
            if Path(file_path).is_absolute():
                errors.append(f"{node_id}.file must be vault-relative")
                continue
            try:
                source = safe_relative_path(link_root, file_path)
                if not source.is_file():
                    errors.append(f"{node_id}.file does not exist: {file_path}")
            except ValueError as exc:
                errors.append(f"{node_id}.{exc}")

    edge_ids: set[str] = set()
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"canvas.edges[{index}] must be an object")
            continue
        edge_id = edge.get("id")
        if not isinstance(edge_id, str) or not edge_id:
            errors.append(f"canvas.edges[{index}].id is required")
        elif edge_id in edge_ids:
            errors.append(f"duplicate canvas edge ID: {edge_id}")
        else:
            edge_ids.add(edge_id)
        for field in ("fromNode", "toNode"):
            if edge.get(field) not in node_ids:
                errors.append(f"{edge_id or index}.{field} references missing node")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Wireframer Canvas structure and file links: OK")
    return 0


def validate_workspace(root: Path, quiet: bool = False) -> int:
    root = root.resolve()
    errors: list[str] = []
    state = root / ".wireframer"
    project = load_json(state / "project.json", errors)
    signals_doc = load_json(state / "signals.json", errors)
    graph_doc = load_json(state / "graph.json", errors)
    manifest = load_json(root / WORKSPACE_MANIFEST, errors)

    for name, doc in (
        ("project", project),
        ("signals", signals_doc),
        ("graph", graph_doc),
        ("workspace", manifest),
    ):
        allowed_versions = (1, 2) if name == "graph" else (1,)
        if doc and doc.get("schemaVersion") not in allowed_versions:
            errors.append(f"{name}.schemaVersion must be one of {allowed_versions}")

    if manifest:
        if manifest.get("managedBy") != "wireframer":
            errors.append("workspace.managedBy must be wireframer")
        if manifest.get("slug") != project.get("slug"):
            errors.append("workspace.slug must match project.slug")
        boundary = Path(manifest.get("cleanupBoundary", root)).resolve()
        if boundary != root and boundary not in root.parents:
            errors.append("workspace.cleanupBoundary must contain the workspace")
        for field in ("generatedFiles", "generatedDirectories"):
            values = manifest.get(field, [])
            if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                errors.append(f"workspace.{field} must be an array of paths")
                continue
            for value in values:
                try:
                    if field == "generatedFiles":
                        safe_relative_path(root, value)
                    else:
                        safe_cleanup_directory(root, boundary, value)
                except ValueError as exc:
                    errors.append(str(exc))

    raw_nodes = graph_doc.get("nodes", [])
    nodes = raw_nodes if isinstance(raw_nodes, list) else []
    if raw_nodes is not nodes:
        errors.append("graph.nodes must be an array")
    graph_version = graph_doc.get("schemaVersion")

    node_types: dict[str, str] = {}
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"graph.nodes[{index}] must be an object")
            continue
        node_id = node.get("id")
        node_type = node.get("type")
        if not isinstance(node_id, str) or not ID_PATTERN.match(node_id):
            errors.append(f"graph.nodes[{index}].id is invalid")
            continue
        if node_id in node_types:
            errors.append(f"duplicate graph ID: {node_id}")
        if not isinstance(node_type, str) or not node_type:
            errors.append(f"{node_id}.type is required")
            continue
        if graph_version == 2:
            for field in ("meaning", "status"):
                if not isinstance(node.get(field), str) or not node[field].strip():
                    errors.append(f"{node_id}.{field} must be a non-empty string")
            classification = node.get("classification")
            if node_type == "product-capability" and (
                not isinstance(classification, str) or not classification.strip()
            ):
                errors.append(f"{node_id}.classification is required for product-capability")
            elif classification is not None and (
                not isinstance(classification, str) or not classification.strip()
            ):
                errors.append(f"{node_id}.classification must be one non-empty value")
        node_types[node_id] = node_type

    for node in nodes:
        if not isinstance(node, dict) or node.get("id") not in node_types:
            continue
        node_id = node["id"]
        links = node.get("links", [])
        if not isinstance(links, list):
            errors.append(f"{node_id}.links must be an array")
            continue
        for linked_id in links:
            if linked_id not in node_types:
                errors.append(f"dangling link: {node_id} -> {linked_id}")

        expected_parent = {"job-story": "human-job", "business-story": "business-job"}.get(
            node_types[node_id]
        )
        if expected_parent:
            parents = [linked_id for linked_id in links if node_types.get(linked_id) == expected_parent]
            if len(parents) != 1:
                errors.append(f"{node_id} must link to exactly one {expected_parent}")

    raw_signals = signals_doc.get("signals", [])
    signals = raw_signals if isinstance(raw_signals, list) else []
    if raw_signals is not signals:
        errors.append("signals.signals must be an array")

    signal_ids: set[str] = set()
    for index, signal in enumerate(signals):
        if not isinstance(signal, dict):
            errors.append(f"signals[{index}] must be an object")
            continue
        signal_id = signal.get("id")
        if not isinstance(signal_id, str) or not re.match(r"^SIG-[0-9]+$", signal_id):
            errors.append(f"signals[{index}].id is invalid")
            continue
        if signal_id in signal_ids:
            errors.append(f"duplicate signal ID: {signal_id}")
        signal_ids.add(signal_id)
        if not isinstance(signal.get("meaning"), str) or not signal["meaning"].strip():
            errors.append(f"{signal_id}.meaning must be a non-empty string")
        if not isinstance(signal.get("authority"), str) or not signal["authority"].strip():
            errors.append(f"{signal_id}.authority must be one non-empty value")
        knowledge_status = signal.get("knowledgeStatus")
        if not isinstance(knowledge_status, str) or knowledge_status not in KNOWLEDGE_STATUSES:
            errors.append(f"{signal_id}.knowledgeStatus is invalid")
        disposition = signal.get("disposition")
        kind = disposition.get("kind") if isinstance(disposition, dict) else None
        if not isinstance(kind, str) or kind not in DISPOSITIONS:
            errors.append(f"{signal_id}.disposition is invalid")
            continue
        refs = disposition.get("refs", [])
        if not isinstance(refs, list):
            errors.append(f"{signal_id}.disposition.refs must be an array")
        elif disposition.get("kind") == "represented":
            if not refs:
                errors.append(f"{signal_id} represented disposition requires refs")
            for ref in refs:
                if not isinstance(ref, str) or ref not in node_types:
                    errors.append(f"{signal_id} references missing graph node: {ref}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if not quiet:
        print("Wireframer workspace structure: OK")
    return 0


def impact_report(root: Path, changed_id: str) -> int:
    """List graph nodes that cite a changed node, directly or transitively."""
    root = root.resolve()
    if validate_workspace(root, quiet=True) != 0:
        return 1
    graph = load_json(root / ".wireframer/graph.json", [])
    nodes = {node["id"]: node for node in graph["nodes"]}
    if changed_id not in nodes:
        print(f"ERROR: graph node does not exist: {changed_id}")
        return 1

    dependents: dict[str, list[str]] = {}
    for node in nodes.values():
        for upstream_id in node.get("links", []):
            dependents.setdefault(upstream_id, []).append(node["id"])

    paths: dict[str, list[str]] = {changed_id: [changed_id]}
    queue = [changed_id]
    for upstream_id in queue:
        for dependent_id in sorted(dependents.get(upstream_id, [])):
            if dependent_id not in paths:
                paths[dependent_id] = paths[upstream_id] + [dependent_id]
                queue.append(dependent_id)

    affected = [
        {"id": node_id, "type": nodes[node_id]["type"], "path": paths[node_id]}
        for node_id in queue[1:]
    ]
    print(json.dumps({"changed": changed_id, "affected": affected}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("root", type=Path)
    init_parser.add_argument("--slug", required=True)
    init_parser.add_argument("--language", default="ru")
    init_parser.add_argument("--active-stage", default="human-jobs")
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("root", type=Path)
    impact_parser = subparsers.add_parser("impact")
    impact_parser.add_argument("root", type=Path)
    impact_parser.add_argument("changed_id")
    canvas_parser = subparsers.add_parser("validate-canvas")
    canvas_parser.add_argument("root", type=Path)
    canvas_parser.add_argument("canvas", type=Path)
    canvas_parser.add_argument("--vault-root", type=Path, help="Actual Obsidian vault root; file links resolve from here")
    track_parser = subparsers.add_parser("track")
    track_parser.add_argument("root", type=Path)
    track_parser.add_argument("paths", nargs="+", type=Path)
    clean_parser = subparsers.add_parser("clean")
    clean_parser.add_argument("root", type=Path)
    clean_parser.add_argument("--slug", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "init":
        return init_workspace(args.root.resolve(), args.slug, args.language, args.active_stage)
    if args.command == "validate":
        return validate_workspace(args.root.resolve())
    if args.command == "impact":
        return impact_report(args.root.resolve(), args.changed_id)
    if args.command == "validate-canvas":
        return validate_canvas(args.root.resolve(), args.canvas, args.vault_root)
    if args.command == "track":
        return track_files(args.root.resolve(), args.paths)
    return clean_workspace(args.root.resolve(), args.slug)


if __name__ == "__main__":
    sys.exit(main())
