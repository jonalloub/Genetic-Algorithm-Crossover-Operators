from random import randint
from collections import Counter

class problem:
    def __init__(self):
        pass

    def individual(self,length, min, max):
        individual = [randint(min, max) for x in range(length)]
        return ''.join(str(item) for item in individual)

    def population(self, size, length, min, max):
        return [self.individual(length, min, max) for x in range(size)]
        #return ["51842736", "32752411"]

    def find_fintness(self, population, max=28):
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
                test = individual_list[i]
                current = individual_list[i]

                for j in range(i + 1, len(individual_list)):
                    current += 1
                    next = individual_list[j]

                    if current >= 9 or current < 1:
                        break

                    if current == next:
                        count += 1

            for i in range(len(individual_list) - 1):
                test = individual_list[i]
                current = individual_list[i]

                for j in range(i + 1, len(individual_list)):
                    current -= 1
                    next = individual_list[j]

                    if current > 9 or current < 1:
                        break

                    if current == next:
                        count += 1
            #print(count)
            fitnessScores[individual] = (max - count)

        return fitnessScores

    def select_for_crossover(self, population, num_of_chromosomes):


        selected_for_crossover = []

        # Find the fitness scores all chromosomes in population
        fitness_scores = self.find_fintness(population)

        # Select the top most, according to number of chromosomes stated for each iteration
        # that is given as input by the user
        selected = dict(Counter(fitness_scores).most_common(num_of_chromosomes))
        print(str(selected) + 'selected')


        # Put all those top chromosome in list for crossover operation
        for keys in selected:
            selected_for_crossover.append(keys)

        #print('selected'+str(selected))
        return selected_for_crossover
