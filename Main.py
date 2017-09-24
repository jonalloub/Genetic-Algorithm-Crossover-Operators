from GeneticAlgoritm import *
from Problem import *


population = ["86427531", "32752411", "24415124", "32543213"]
#population = [24748552, 32752411, 24415124, 32543213]

problem = problem()
population = problem.population(100,8,1,8)

#print(population)
result = genetic_search(problem, population)
print(str(result) + " :end")
