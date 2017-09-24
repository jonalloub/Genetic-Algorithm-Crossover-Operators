import math
from random import randint, random
from copy import copy

def mut(population):
    chance_to_mutate = 0.7
    result = []

    for chromosome in population:
        if chance_to_mutate > random():
            place_to_mutate = randint(0, len(chromosome)-1)
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

def single_point_cross_over(population):

    crossover_population = []

    # Get parents
    parent_male, parent_female = select_parents(population)

    # Performing crossover operation
    # If the even split operation did not function properly stop program

    for female in parent_female:
        male = copy(list(parent_male))
        female = list(female)

        # Randomly generating crossover point
        crossover_point = randint(1 , 6)

        # Crossing over from randomly generated point
        male[crossover_point:], female[crossover_point:] = \
            female[crossover_point:], male[crossover_point:]

        crossover_population.append(''.join(str(item) for item in male))
        crossover_population.append(''.join(str(item) for item in female))


    crossover_population = mut(crossover_population)
    return crossover_population


def two_point_cross_over(population):
    crossover_population = []

    # Randomly select the two crossover points
    crossover_points = [randint(1, 7)]

    second_point = randint(1, 7)
    while second_point == crossover_points[0]:
        print("here")
        second_point = randint(1, 7)

    crossover_points.append(second_point)
    print(crossover_points)

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


    crossover_population = mut(crossover_population)
    return crossover_population


def uniform_point_cross_over():
    pass

def cut_and_splice_cross_over(population):
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
        var = list((randint(1,8) for x in range(len(male), 8)))
        male.extend(var)
        var = list((randint(1, 8) for x in range(len(female), 8)))
        female.extend(var)

        # To ensure list is not bigger than 8 digits
        del male[8:]
        del female[8:]

        crossover_population.append(''.join(str(item) for item in male))
        crossover_population.append(''.join(str(item) for item in female))

    crossover_population = mut(crossover_population)
    return crossover_population


def genetic_search(problem, population, max=-1):

    iteration = 0
    while max != 0:
        iteration += 1
        fitnessScores = problem.find_fintness(population)

        for key, value in fitnessScores.items():
            if value == 28:
                return {key : iteration}

        selected_for_crossover = problem.select_for_crossover(population, 20)

        #population = single_point_cross_over(selected_for_crossover)
        #population = two_point_cross_over(selected_for_crossover)
        population = cut_and_splice_cross_over(selected_for_crossover)


        max = max -1



