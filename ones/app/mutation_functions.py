
from ones.app.m import choose_random_index,choose_random_value

def mutate_individual(individual:list, mutate_percentage:int ):
    index = choose_random_index(individual, mutate_percentage)
    mutated_individual = individual.copy()
    for i in index:
        value = choose_random_value([0,1])
        mutated_individual[i] = value
    
    return mutated_individual


