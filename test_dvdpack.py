# coding:utf-8

import unittest
from dvdpack import sober_knapsack, get_args

class DVDPackTest(unittest.TestCase):

  items = [
    (1653484, 'AmeKimi/ep01_03'),
    (  35964, 'ChiiKawa/ep124'),
    ( 728548, 'ClassicStars/ep13'),
    ( 729600, 'Clevatess/ep02'),
    ( 566128, 'Danjoru/ep10'),
    (  98192, 'GalaxyExpress/ep12'),
    ( 703704, 'HikaNatsu/ep02'),
    ( 776164, 'Kijin/ep15'),
    ( 577440, 'Mizuzokusei/ep03'),
    ( 730400, 'Mynoghra/ep01'),
    (1715772, 'Nageki/ep01_03'),
    ( 556768, 'Naruto/ep547'),
    (  63644, 'ShibuyaHachi/ep37'),
    (1730764, 'SilentWitch/ep01_03'),
    (  26568, 'SumikkoGurashi/ep11'),
    ( 730304, 'SummerPockets/ep14'),
    ( 726760, 'Takopi/ep04'),
    (1715436, 'TenseiSoushu/ep01_03'),
    ( 573632, 'TougenAnki/ep01'),
    ( 728724, 'TsuihoshaShokudo/ep01'),
    (1160464, 'WitchWatch/ep13_14'),
  ]
  expected = [(4586996.0, [0, 1, 4, 5, 7, 15, 16])]

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_solve(self):
    """solve knapsack problem"""
    result = sober_knapsack(self.items, get_args())
    self.assertEqual(self.expected, result)

if __name__ == "__main__":
    unittest.main()
