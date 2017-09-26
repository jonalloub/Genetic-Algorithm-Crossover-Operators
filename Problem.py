from collections import Counter
from random import randint


class problem:
    def __init__(self, num_of_chromosomes, chance_to_mutate, iteration, crossover_type):
        self.num_of_chromosomes = int(num_of_chromosomes)
        self.chance_to_mutate = float(chance_to_mutate)
        self.iteration = int(iteration)
        self.crossover_type = int(crossover_type)

    def individual(self, length, min, max):
        individual = [randint(min, max) for x in range(length)]
        return ''.join(str(item) for item in individual)

    def population(self, size, length, min, max):
        return [self.individual(length, min, max) for x in range(size)]

    def find_fitness(self, population, max=28):
        # This function was based off of https://gist.github.com/kkweon/f86def6ea240ca9c72c25f3d09bd0df3

        fitnessScores = {}

        for individual in population:
            count = 0
            individual_list = [int(x) for x in individual]

            for i in range(len(individual_list) - 1):
                current = individual_list[i]

                for j in range(i + 1, len(individual_list)):
                    next = individual_list[j]

                    if current == next:
                        count += 1

            for i in range(len(individual_list) - 1):
                current = individual_list[i]

                for j in range(i + 1, len(individual_list)):
                    current += 1
                    next = individual_list[j]

                    if current >= 9 or current < 1:
                        break

                    if current == next:
                        count += 1

            for i in range(len(individual_list) - 1):
                current = individual_list[i]

                for j in range(i + 1, len(individual_list)):
                    current -= 1
                    next = individual_list[j]

                    if current > 9 or current < 1:
                        break

                    if current == next:
                        count += 1

            fitnessScores[individual] = (max - count)
        fitnessScores = dict(Counter(fitnessScores).most_common())
        return fitnessScores

    def select_for_crossover(self, population, num_of_chromosomes):

        selected_for_crossover = []

        # Find the fitness scores all chromosomes in population
        fitness_scores = self.find_fitness(population)

        # Select the top most, according to number of chromosomes stated for each iteration
        # that is given as input by the user
        selected = dict(Counter(fitness_scores).most_common(num_of_chromosomes))

        for keys in selected:
            selected_for_crossover.append(keys)

        return selected_for_crossover
