import unittest 
import ones.app.mutation_functions as mtf
import ones.app.m as m


class TestMutationFunctions(unittest.TestCase):
    
    def test_mutate_individual(self):
        m.init_seed(2)
        individual = [1,1,1,1]
        
        result = mtf.mutate_individual(individual,50)
        self.assertEqual([1,0,1,0], result, "should be mutated")

