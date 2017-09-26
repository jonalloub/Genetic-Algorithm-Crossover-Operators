from GeneticAlgoritm import *
from Problem import *

data = input("\nPlease enter the following values seperated by spaces:\n"
             "\n- Initial population size, \n"
             "- Number of chromosomes to select at each iteration or generation of the GA \n"
             "- Mutation rate \n"
             "- Number of iterations or generations to run the GA for; -1 to run the GA until a goal state is found. d \n"
             "\nExample: 100 20 0.7 100 \n"
             "\nEnter your input (enter ! to exit): ")

if data == "!":
    exit()

crossover_type = input("\nSelect your cross over operator:\n"
                       "0 - Single Crossover\n"
                       "1 - Two Points Crossover\n"
                       "2 - Cut and Splice Crossover\n"
                       "3 - Uniform Crossover\n"
                       "\nEnter your input (enter ! to exit):")

if crossover_type == "!":
    exit()

params = (data.strip()).split()
crossover_type.strip()
params.append(crossover_type)

if len(params) < 5:
    print("\nNot enough inputs were provided")
    exit()

problem = problem(params[1], params[2], params[3], params[4])
population = problem.population(int(params[0]), 8, 1, 8)

result = genetic_search(problem, population)

crossover = ["Single Point", "Two Points", "Cut and Splice", "Uniform"]
print("Initial Population:{0}, Number of Chromosomes:{1}, Mutation Rate:{2}, "
      "Max number of Iteration:{3}, Crossover Type:{4}".format(params[0], params[1],
                                                               params[2], params[3], crossover[int(params[4])]))
print("\n- Number of Generations: {0}".format(result[3]))
if result[0] == False:
    print("\n***Answer not reached, ran out of iterations! Try increasing the values of your inputs***")
    print("- Highest State: {0}".format(str(result[1])))
    print("- Highest State Fitness Value: {0}".format(result[2]))

else:
    print("- Final State: {0}".format(str(result[1])))
    print("- Final State Fitness Value: {0}".format(result[2]))
