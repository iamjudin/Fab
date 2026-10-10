import importlib.util,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('structure_guard',Path(__file__).resolve().parents[1]/'plugins/fab/skills/wireframe/scripts/check_structure.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def n(id,kind,x,y,w,h,**extra):return dict(id=id,type=kind,x=x,y=y,width=w,height=h,**extra)
class StructureTests(unittest.TestCase):
    def test_flat_labels_do_not_prove_ownership(self):
        c={'nodes':[n('screen','text',0,0,200,70,text='S-01 main'),n('action','text',0,100,200,50,text='S-01 open')],'edges':[{'id':'open','fromNode':'action','toNode':'screen'}]}
        self.assertTrue(m.check(c,['S-01']))
    def test_real_group_with_control_origin_is_valid(self):
        c={'nodes':[n('screen','group',0,0,300,250,label='S-01 main'),n('action','text',20,70,200,50,text='Open')],'edges':[{'id':'open','fromNode':'action','toNode':'screen'}]}
        self.assertEqual(m.check(c,['S-01']),[])
    def test_control_outside_declared_owner_is_rejected(self):
        c={'nodes':[n('screen','group',0,0,300,250,label='S-01 main'),n('info','text',20,20,200,50),n('action','text',350,20,200,50)],'edges':[{'id':'open','fromNode':'action','toNode':'screen'}]}
        self.assertTrue(m.check(c,['S-01']))
    def test_flow_only_is_not_run_as_structure_implicitly(self):
        self.assertEqual(m.check({'nodes':[n('step','text',0,0,200,70)],'edges':[]},[]),[])

    def test_app_navigation_can_have_one_separate_owner(self):
        c={'nodes':[n('screen','group',0,0,300,250,label='S-01 main'),n('info','text',20,20,200,50),n('global-navigation','group',350,0,300,150,label='App tabs'),n('tab','text',370,40,200,50)],'edges':[{'id':'open','fromNode':'tab','toNode':'screen'}]}
        self.assertEqual(m.check(c,['S-01']),[])
