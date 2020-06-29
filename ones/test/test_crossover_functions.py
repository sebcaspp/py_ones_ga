import unittest
import ones.app.crossover_functions as csf
import ones.app.m as m

class TestCrossoverFunctions(unittest.TestCase):

    def test_cross_indivuduals(self):
        m.init_seed(1)
        individual_x = [1,1,1,1]
        individual_y = [0,0,0,0]

        result = csf.cross_indivuduals(individual_x, individual_y, 50)
        self.assertEqual([0,1,1,0], result, "cross_indivuduals should cross two individuals")