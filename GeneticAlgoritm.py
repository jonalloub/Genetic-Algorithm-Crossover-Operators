from Problem import *
import math
from random import randint



def crossover():
    pass

def mutate():
    pass



def single_point_cross_over(population):

    # Evenly splitting population into male and female
    parent_male = population[:int(math.ceil(len(population) / 2))]
    parent_female = population[int(math.floor(len(population) / 2)):]

    # Performing crossover operation
    # If the even split operation did not function properly stop program
    if len(parent_female) == len(parent_male):
        for male, female in zip (parent_male, parent_female):
            male = list(male)
            female = list(female)

            # Randomly generating crossover point
            crossover_point = randint(0 , 7)

            # Crossing over from randomly generated point
            male[crossover_point:], female[crossover_point:] = \
                female[crossover_point:], male[crossover_point:]

    else:
        print("Your slicing did not function properly")
        exit()




    pass

def two_point_cross_over():
    pass

def uniform_point_cross_over():
    pass

def cut_and_splice_cross_over():
    pass
