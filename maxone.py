# maxone.py
# Author: Sébastien Combéfis
# Version: April 26, 2020

import random
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

IND_SIZE = 15
POP_SIZE = 100

# Initialising the population.
population = []

# Defining the fitness function.
def evaluate(ind):
    return sum(ind)

# Defining the mating function.
def mate(ind1, ind2):
    assert len(ind1) == len(ind2), "ind1 & ind2 should be the same length"

    for i in range(len(ind1)):
        if random.random() >= PROB_MATING:
            ind1[i], ind2[i] = ind2[i], ind1[i]

    return ind1, ind2

# Defining the mutation function.
def mutate(ind):
    for i in range(len(ind)):
        if random.random() >= PROB_MUTATION:
            random_gene = random.randint(0, len(ind)-1)
            ind[i], ind[random_gene] = ind[random_gene], ind[i]
            break

    return ind

# Defining the selection function.
def select(pop):
    parents = list()

    all_fitness = [sum(individual) for individual in pop]

    for i in range(2):
        pop_sum = 0
        limit = random.randint(0, len(pop))
        
        for index, fitness_value in enumerate(all_fitness):
            pop_sum += fitness_value

            if pop_sum > limit:
                parents.append(pop[index])
                break

            if index == len(all_fitness)-1:
                parents.append(pop[index])

    return tuple(parents)


# Running the simulation.
if __name__ == '__main__':
    PROB_MATING = 0.5
    PROB_MUTATION = 0.2
    ITERATIONS = 150

    # Create initial population
    for i in range(POP_SIZE):
        population.append([random.randrange(2) for i in range(IND_SIZE)])


    stats = list()
    for i in range(ITERATIONS):
        parents = select(population)
        children = mate(parents[0], parents[1])
        mutate_children = list(map(mutate, children))

        for j in range(2):
            iteration_fitness = list(map(evaluate, population))
            del population[iteration_fitness.index(min(iteration_fitness))]

        for child in mutate_children:
            population.append(child)

        iteration_fitness = np.array(list(map(evaluate, population)))
        stats.append((i+1, np.mean(iteration_fitness), np.min(iteration_fitness), np.max(iteration_fitness)))


    print(tabulate(stats, headers=['Gen', 'Mean', 'Min', 'Max']))

    print("Final population:\n", '\n'.join('{}: {}'.format(individual, evaluate(individual)) for individual in population), '\n')

    plt.plot(np.arange(ITERATIONS), [stat[1] for stat in stats])
    plt.show()