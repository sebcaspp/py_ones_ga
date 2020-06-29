import unittest
import ones.app.m as m

class TestM(unittest.TestCase):

    def test_choose_n_from_list(self):
        m.init_seed(2)

        result = m.choose_n_from_list([1,2,3,4], 2)
        self.assertEqual([4,2], result, "choose_n_from_list should choose 2 elements from the list")