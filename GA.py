import random
from Chromosome import Chromosome

def initPopulation():
    P = []
    Psize = 1000
    numGenes = 5

    for i in range(Psize):
        s = ""
        for j in range(numGenes):
            s += str(random.randint(0, 1))
        ch = Chromosome(s)
        P.append(ch)

    sumF = 0
    print("Initial Population:")
    for i, chromosome in enumerate(P):
        chromosome.fitness = fitness(chromosome)
        sumF += chromosome.fitness
        if (i % 10 == 0):
            print(f"genome: {chromosome}, value: {int(chromosome.gene, 2)}, fitness: {chromosome.fitness}")
    print(f"Average fitness: {sumF/Psize}")
    return P

# ===============================================
# ===============================================

def fitness(chromosome):
    days = int(chromosome.gene, 2)
    fitness = 0
    if (days <= 31):
        fitness = (100 * days)
        if (days > 21):
            fitness -= (5 * ((days-20)**2) )
    return fitness

# ===============================================
# ===============================================

def towerSample(P):
    sumF = 0
    r = random.random()
    for chromosome in P:
        sumF += chromosome.normFitness
        if (sumF > r):
            selected = chromosome
            break
    return selected

# ===============================================
# ===============================================

def crossOver(P):
    r1 = random.randint(0, len(P)-1)
    r2 = random.randint(0, len(P)-1)
    while (r2 == r1):
        r2 = random.randint(0, len(P)-1)

    p1 = P[r1]
    p2 = P[r2]

    locus = 3

    p1Segment = p1.gene[locus:]
    p2Segment = p2.gene[locus:]

    p1.alterGene = p1.gene[:locus] + p2Segment
    p2.alterGene = p2.gene[:locus] + p1Segment

    return P

# ===============================================
# ===============================================

def mutate(P):
    chrom = P[random.randint(0, len(P)-1)]
    index = random.randint(0, len(chrom.gene)-1)
    tempStr = chrom.gene

    if (tempStr[index] == "0"):
        tempStr = tempStr[:index] + "1" + tempStr[index+1:]
    else:
        tempStr = tempStr[:index] + "0" + tempStr[index+1:]

    chrom.gene = tempStr

    return P

# ===============================================
# ===============================================

def operate(P):
    if (random.random() < 0.8):
        P = crossOver(P)
    if (random.random() <= 0.01):
        P = mutate(P)
    return P
