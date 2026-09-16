"""Regression for combat options pruned before long-term evaluation."""
import unittest
from unittest.mock import patch
from strategic_planner import candidates

class SearchAssessmentTests(unittest.TestCase):
 def test_low_immediate_combat_value_does_not_remove_combat_family(self):
  # A cheap repair can rank first while an attack opens a future capture.
  # Every legal combat family must still reach the rollout evaluator.
  options=[('expand',0),('move',0,1),('ground',(0,),0),
           ('ground_mobile',(0,),1,0),('naval',(0,),0,1),
           ('bombard_shared',(0,),0),('none',)]
  class Stub:
   selected=None
   def actions(self,*args,**kwargs):return options
   def act(self,p,order,*args,**kwargs):self.selected=order
  arena=Stub()
  with patch('strategic_planner.clone',side_effect=lambda a:Stub()),patch('strategic_planner.score',side_effect=lambda a,p,policy:100 if a.selected[0]=='expand' else 0):
   kept=candidates(arena,0,'fleet','balanced',0,1)
  for kind in ('ground','ground_mobile','naval','bombard_shared'):
   self.assertTrue(any(o[0]==kind for o in kept),kind)

if __name__=='__main__':unittest.main()
