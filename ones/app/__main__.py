import ones.app.ones_ga as ga

def main():
    r = ga.run_ga(n = 20, m = 50, gene_options = [0,0],
           number_best_individuals = 10,        
           offprings_number = 20,
           survival_number = 10,
           crossover_percentage = 50, 
           mutation_percentage = 20, 
           number_generations = 10) 
    print(r)


if __name__ == "__main__":
    main()
