
import random 
from functools import reduce

seed = "semilla2"
random.seed(a=seed)


n = 20
m = 10
gene_options = [0,0,0,1]

def generate_pupulation(n: int, m: int,gene_options:[])-> [[]]:
    individual = lambda n:random.choices( gene_options, k= n )    
    return [ individual(n) for i in range(m) ]  

def eval_fitnes(population: []): 
    for individual in population:
        score = reduce( lambda x,y: x+y, individual)
        yield (score, individual)

def mutate_individual(individual:list, mutate_percentage:int = 40 ):
    mutation_number = int((len(individual) * mutate_percentage)/100)
    index = random.choices( list(range(len(individual))), k=mutation_number)
    mutated_individual = individual.copy()
    for i in index:
        if individual[i] == 0: 
            mutated_individual[i] = 1
        else: 
            mutated_individual[i] = 0

    return mutated_individual

def cross_indivuduals(individual_x: list, individual_y: list) -> list: 
    crossover_percentage = 50
    number_of_genes = int( (crossover_percentage * len(individual_x) ) / 100 )
    index = random.choices( range( len(individual_x) ) , k= number_of_genes )
    offpring = individual_y.copy()
    for i in index:
        offpring[i] = individual_x[i]
    return offpring

def f(population, crossover_percentage, survival_percentage, mutate_percentage) -> list:
    cross_number = int( (crossover_percentage * len(population)*2 ) / (100*2) ) +1
    
    cross_index = random.choices( range(cross_number), k= int(cross_number/2) )
    rest_cross_index = filter( lambda i: i in cross_index ,range(cross_number))

    survival_index = int( len(population)*survival_percentage/100 ) 

    mutation_percentage = (100 - crossover_percentage -survival_percentage)/100
    mutations_number  = int(mutation_percentage*len(population)) + 1
    mutation_index = random.choices( range(len(population)), k= mutations_number )

    print("cross_index->", cross_index)
    print("rest_cross->", rest_cross_index)

    new_population = []
    for x,y in zip(cross_index, rest_cross_index):
        offpring = cross_indivuduals(population[x], population[y])
        print("---crossover---")
        print("individuo x -> ", population[x])
        print("individuo y -> ", population[y])
        print("offpring    -> ", offpring)

        offpring = mutate_individual(offpring, 10)
        print("offpring mut-> ", offpring)
        print("---end--- " )
        new_population.append(offpring) 

    
    for i in mutation_index:
        mutated_individual = mutate_individual(population[i],mutate_percentage)
        new_population.append(mutated_individual)
        
    new_population.extend( population[:survival_index] )
    return new_population

def print_sorted_score(score):
    for s in score:
        print("score -> ", s[0])
        print("individual -> ", s[1])

def run_ga(crossover_percentage, mutation_percentage, survival_percentage,number_generations:int = 10):
    
    population = generate_pupulation(n, m, gene_options)
    best_results = []
    for g in range(number_generations):
        scores =  eval_fitnes(population)
        sorted_scores = sorted(scores, key=lambda tup: tup[0], reverse= True) 
        
        print("----generacion ", g, "-----")
        print_sorted_score(sorted_scores)
        
        best_results.append(sorted_scores[0][0])
        sorted_individuals = [ individual for score, individual in sorted_scores ]
        population = f(sorted_individuals, crossover_percentage, survival_percentage, mutation_percentage)

    return best_results

"""
results = []
for survival_percentage in range(0,100,5):
    for crossover_percentage in range(100-survival_percentage, 0, -5):
        for mutation_percentage in range(100-crossover_percentage-survival_percentage, 0, -5):
            best_results=run_ga(crossover_percentage, mutation_percentage, survival_percentage)
            results.append([crossover_percentage, mutation_percentage, survival_percentage, best_results])


with open("results","w") as file: 
    for r in results:
        file.write( str(r) + "\n")
        if r[3][len(r[3])-1] == n:
            print(r)

"""

print(run_ga(10, 25, 45, 10))





