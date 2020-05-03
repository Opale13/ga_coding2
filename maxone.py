# maxone.py
# Author: Sébastien Combéfis
# Version: April 26, 2020

import random

IND_SIZE = 10
POP_SIZE = 6

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
    ITERATIONS = 100

    INIT_POPULATION = 10
    INDIVIDUAL_LENGTH = 5

    for i in range(INIT_POPULATION):
        population.append([random.randrange(2) for i in range(INDIVIDUAL_LENGTH)])
    

    # for individual in population:
    #     print("{} - {}".format(individual, evaluate(individual)))


    parents = select(population)
    print("Parents: {}".format(parents))
    # print("Children: {}".format(mate(parents[0], parents[1])))
    print("Mutation of parent 0: {}".format(mutate(parents[0])))
    