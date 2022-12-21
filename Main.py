from Chromosome import Chromosome
import GA

def printFinalGeneration(P):
    print("Final Generation =====================================")
    sumDays = 0
    for ch in P:
        sumDays += int(ch.gene, 2)
        print(f"string: {ch}, value: {int(ch.gene, 2)}, fitness: {ch.fitness}")
    print(f"Average final value: {sumDays/len(P)}")

# ===============================================
# ===============================================

def iterate(P, t, maxT):
    t += 1
    if (t > maxT):
        printFinalGeneration(P)
        return
    print(f"Generation: {t} ==========================")

    totalFitness    = 0
    maxFitness      = 0

    for chromosome in P:
        f = GA.fitness(chromosome)
        chromosome.fitness = f
        totalFitness += f
        if (f > maxFitness):
            maxFitness = f

    for chromosome in P:
        if (totalFitness == 0):
            normFitness = 0
        else:
            normFitness = chromosome.fitness / totalFitness
        chromosome.normFitness = normFitness

    Pnext = []
    for i in range(len(P)):
        Pnext.append(GA.towerSample(P))

    Pnext = GA.operate(Pnext)
    print(f"Max Fitness: {maxFitness}")
    print(f"Avg Fitness: {totalFitness/len(P)}")
    iterate(Pnext, t, maxT)

# ===============================================
# ===============================================

P = GA.initPopulation()

t = 0
maxT = 50
iterate(P, t, maxT)
