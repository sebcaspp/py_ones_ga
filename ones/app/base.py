
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




