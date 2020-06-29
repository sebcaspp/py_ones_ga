from typing import List

from ones.app.m import choose_random_index


def cross_indivuduals(individual_x: List[int], individual_y: List[int], crossover_percentage:int ) -> List[int]: 
    index = choose_random_index(individual_x, crossover_percentage)
    offpring = individual_y.copy()
    for i in index:
        offpring[i] = individual_x[i]
    return offpring