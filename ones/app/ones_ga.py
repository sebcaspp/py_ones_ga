from typing import List,Tuple
from functools import reduce

from ones.app.m import choose_n_from_list, choose_random_index, choose_random_value
from ones.app.crossover_functions import cross_indivuduals
from ones.app.mutation_functions import mutate_individual


def generate_pupulation(n: int, m: int, gene_options:List[int])-> List[List[int]]:
    individuals = [ choose_n_from_list(gene_options, n) for i in range(m) ]  
    return individuals

def eval_fitnes(population: List[int])-> Tuple[int, List[int]]: 
    for individual in population:
        score = reduce( lambda x,y: x+y, individual)
        yield (score, individual)

def generate_new_population( population: List[List[int]], 
                             number_best_individuals: int,        
                             offprings_number: int,                       
                             survival_number: int,
                             crossover_percentage: int,                                                            
                             mutation_percentage: int ) -> List[List[int]]:
                             
    best_individuals:List[List[int]] = population[:number_best_individuals]
    index_best_individuals = list(range(number_best_individuals))
    new_population = []
    for _ in range(offprings_number):
        x = choose_random_value(index_best_individuals)
        y = choose_random_value(index_best_individuals)
        offpring = cross_indivuduals(best_individuals[x], best_individuals[y], crossover_percentage)
        offpring = mutate_individual(offpring, mutation_percentage)
        new_population.append(offpring) 
    
    remaining_population = len(population) - number_best_individuals - survival_number
    index_remaining_population = list( range(survival_number+1,len(population)) )
    for _ in range(remaining_population):
        i = choose_random_value(index_remaining_population)
        mutated_individual = mutate_individual(population[i], mutation_percentage)
        new_population.append(mutated_individual)
        
    new_population.extend( population[:survival_number] )
    return new_population

def run_ga(n:int, m:int, gene_options: List[int], 
           number_best_individuals: int,        
           offprings_number: int,
           survival_number:int,
           crossover_percentage:int, 
           mutation_percentage, 
           number_generations:int = 10):
    
    population = generate_pupulation(n, m, gene_options)
    best_results = []
    for _ in range(number_generations):
        scores =  eval_fitnes(population)
        sorted_scores = sorted(scores, key=lambda tup: tup[0], reverse= True) 
        best_results.append(sorted_scores[0][0])
        sorted_individuals = [ individual for score, individual in sorted_scores ]
        population = generate_new_population(sorted_individuals, number_best_individuals, offprings_number, survival_number, crossover_percentage, mutation_percentage)

    return best_results
