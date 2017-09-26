from copy import copy
from random import randint, random


def mut(problem, population):
    chance_to_mutate = float(problem.chance_to_mutate)
    result = []

    for chromosome in population:
        if chance_to_mutate > random():
            place_to_mutate = randint(0, len(chromosome) - 1)
            chromosome = list(chromosome)
            chromosome[place_to_mutate] = randint(1, 7)
            chromosome = (''.join(str(item) for item in chromosome))

        result.append(chromosome)

    return result


def select_parents(population):
    # Have the top chromosome mate with the rest
    parent_male = population[0]
    parent_female = population[1:]

    return [parent_male, parent_female]


def single_point_cross_over(problem, population):
    crossover_population = []

    # Get parents
    parent_male, parent_female = select_parents(population)

    # Performing crossover operation
    # If the even split operation did not function properly stop program

    for female in parent_female:
        male = copy(list(parent_male))
        female = list(female)

        # Randomly generating crossover point
        crossover_point = randint(1, 6)

        # Crossing over from randomly generated point
        male[crossover_point:], female[crossover_point:] = \
            female[crossover_point:], male[crossover_point:]

        crossover_population.append(''.join(str(item) for item in male))
        crossover_population.append(''.join(str(item) for item in female))

    crossover_population = mut(problem, crossover_population)
    return crossover_population


def two_point_cross_over(problem, population):
    crossover_population = []

    # Randomly select the two crossover points
    crossover_points = [randint(1, 7)]

    second_point = randint(1, 7)
    while second_point == crossover_points[0]:
        second_point = randint(1, 7)

    crossover_points.append(second_point)

    # Get parents
    parent_male, parent_female = select_parents(population)

    for female in parent_female:
        male = copy(list(parent_male))
        female = list(female)

        male[:crossover_points[0]], female[:crossover_points[0]] = \
            female[:crossover_points[0]], male[:crossover_points[0]]

        male[crossover_points[1]:], female[crossover_points[1]:] = \
            female[crossover_points[1]:], male[crossover_points[1]:]

        crossover_population.append(''.join(str(item) for item in male))
        crossover_population.append(''.join(str(item) for item in female))

    crossover_population = mut(problem, crossover_population)
    return crossover_population


def uniform_point_cross_over(problem, population):
    crossover_population = []

    # Get parents
    parent_male, parent_female = select_parents(population)

    # Performing crossover operation
    # If the even split operation did not function properly stop program

    for female in parent_female:
        male = copy(list(parent_male))
        female = list(female)

        # Checking if gene should be mutated
        # Mutation if yes
        for gene in male:
            probability_of_swap = 0.5
            if random() > probability_of_swap:
                index = male.index(gene)
                male[index], female[index] = female[index], male[index]

                crossover_population.append(''.join(str(item) for item in male))
                crossover_population.append(''.join(str(item) for item in female))

    crossover_population = mut(problem, crossover_population)
    return crossover_population


def cut_and_splice_cross_over(problem, population):
    crossover_population = []

    # Get parents
    parent_male, parent_female = select_parents(population)

    # Performing crossover operation
    # If the even split operation did not function properly stop program

    for female in parent_female:
        male = copy(list(parent_male))
        female = list(female)

        # Randomly generating crossover point
        crossover_points = [randint(1, 6), randint(1, 6)]

        # Crossing over from randomly generated point
        male[crossover_points[0]:], female[crossover_points[1]:] = \
            female[crossover_points[1]:], male[crossover_points[0]:]

        # To ensure list in not smaller than 8
        var = list((randint(1, 8) for x in range(len(male), 8)))
        male.extend(var)
        var = list((randint(1, 8) for x in range(len(female), 8)))
        female.extend(var)

        # To ensure list is not bigger than 8 digits
        del male[8:]
        del female[8:]

        crossover_population.append(''.join(str(item) for item in male))
        crossover_population.append(''.join(str(item) for item in female))

    crossover_population = mut(problem, crossover_population)
    return crossover_population


def genetic_search(problem, population):
    # The final result (Top scorer), result[0] True if value found, false otherwise
    result = ["", "", "", ""]

    # Defined numbers of iterations
    max = problem.iteration

    # Counter for iteration
    iteration = 0

    while max != 0:
        iteration = iteration + 1
        fitnessScores = problem.find_fitness(population)

        for key, value in fitnessScores.items():

            if value == 28:
                result[0] = True
                result[1] = key
                result[2] = value
                result[3] = iteration
                return result

        selected_for_crossover = problem.select_for_crossover(population, problem.num_of_chromosomes)

        for key, value in fitnessScores.items():
            result[0] = False
            result[1] = key
            result[2] = value
            result[3] = iteration
            break

        if problem.crossover_type == 0:
            population = single_point_cross_over(problem, selected_for_crossover)
        elif problem.crossover_type == 1:
            population = two_point_cross_over(problem, selected_for_crossover)
        elif problem.crossover_type == 2:
            population = cut_and_splice_cross_over(problem, selected_for_crossover)
        elif problem.crossover_type == 3:
            population = uniform_point_cross_over(problem, selected_for_crossover)
        else:
            print("Crossover Type code not recongnized")
            exit()

        max = max - 1

    return result
