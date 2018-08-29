from random import *
from copy import deepcopy
from math import exp


jobMatrix = [[0,12,10],             # jobMatrix shows the required time for passing from one job to another.
             [4,0,8],               # Required time for passing from job2 to job1 is equal to " jobMatrix[1][0] ".
             [6,10,0]]

machineMatrix = [[10,4,8],          # machineMatrix is defined in pdf.
                 [12,9,5]]

temparature = 10000
cooling_rate = 0.003
initialSolution = [-1, 3, 2, 1]     # Initial Solution



def createNeighbourSolution(currentSolution):

    # neighbourSolution like [2, 3, -1, 1] jobs before -1 belongs to the machine1, others to machine2
    neighbourSolution = deepcopy(currentSolution)

    # lists are zero-based index, our solution array has 4 elements.
    r1 = randint(0,3)
    r2 = randint(0,3)

    # if r1 == r2 then, we need different r2. When they are same, there will be no swapping.
    while r1 == r2:
        r2 = randint(0,3)

    # swapping operation "the orders of job" and "the orders of machines"
    neighbourSolution[r1], neighbourSolution[r2] = neighbourSolution[r2], neighbourSolution[r1]

    #  neigbour solution can be like [2, 1, -1, 3].
    return neighbourSolution

def calculateMachineCost(machine, machineName):

    if machineName == "machine1":
        m = 0
    elif machineName == "machine2":
        m = 1

    length_machine = len(machine)
    cost_machine = 0


    if length_machine > 0:          # Then, machine has any job to do, otherwise there will be no cost.
        i = 0
        while i < length_machine:
            cost_machine += machineMatrix[ m ][ machine[i]-1 ]
            i += 1

    return cost_machine

def calculateJobCost(machine):
    # If there are more than one job, there will be a "cost" because the jobs are waiting for each other.

    length_machine = len(machine)
    cost_job = 0

    if length_machine == 2:
        cost_job = jobMatrix[machine[0] - 1][machine[1] - 1]
    elif length_machine == 3:
        cost_job = jobMatrix[machine[0] - 1][machine[1] - 1] + jobMatrix[machine[1] - 1][machine[2] - 1]

    return cost_job

def cost(solution):

    # Assume that solution is [2, 1, -1, 3].
    # machine1 is going to execute job2 and job1 RESPECTIVELY so, job1 waits job2. This cost also be considered.
    # machine is going to execute job3.

    machine1 = []       # This list will hold the jobs which is going to be executed by machine1.
    machine2 = []       # This list will hold the jobs which is going to be executed by machine2.


    # Specifying jobs for machine1 and machine2. Remember, "-1" was the delimeter.
    i = 0
    while i < len(solution):
        if solution[i] == -1:
            break
        machine1.append(solution[i])
        i+=1

    i += 1

    while i < len(solution):
        machine2.append(solution[i])
        i+=1
    # Specifying jobs for machine1 and machine2. Remember, "-1" was the delimeter.


    cost_machine1 = calculateMachineCost(machine1, "machine1")
    jobCost_machine1 = calculateJobCost(machine1)
    totalCost_machine1 = cost_machine1 + jobCost_machine1

    cost_machine2 = calculateMachineCost(machine2, "machine2")
    jobCost_machine2 = calculateJobCost(machine2)
    totalCost_machine2 = cost_machine2 + jobCost_machine2


    if totalCost_machine1 < totalCost_machine2:
        maxCostMachine = totalCost_machine2
    else:
        maxCostMachine = totalCost_machine1

    return maxCostMachine



# --------      Simulated Annealing Algorithm     -------- #

currentSolution = deepcopy(initialSolution)
bestSolution = deepcopy(currentSolution)


while temparature > 1:

    newSolution = createNeighbourSolution(currentSolution)

    print(currentSolution, cost(currentSolution))

    if cost(newSolution) <= cost(currentSolution):
        currentSolution = newSolution
        if cost(newSolution) <= cost(bestSolution):
            bestSolution = deepcopy(newSolution)

    elif exp( (cost(currentSolution) - cost(newSolution)) / temparature) > uniform(0,1):
        currentSolution = newSolution

    temparature *= 1 - cooling_rate         # temperature is cooling down proportional to the cooling_rate


print(bestSolution, cost(bestSolution))
