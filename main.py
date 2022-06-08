import random
import matplotlib.pyplot as plt


a, b, c, d = map(int, input().split())

def cubic(a: int, b: int, c: int, d: int, x: int):
    return a*x^3+b*x^2+c*x-d

def oneMaxFitness(listi: list , a: int, b: int, c: int, d: int):
    fit = [0, 0, 0]
    for i in range(2):
        fit[i] = cubic(a, b, c, d, listi[i])
    return abs(fit[0])+abs(fit[1])+abs(fit[2])

def individualCreator():
    listi : list = [0, 0, 0]
    listi[0] = random.randint(-10, 10)
    listi[1] = random.randint(-10, 10)
    listi[2] = random.randint(-10, 10)
    return listi

def popCreator(n=200):
    return list([individualCreator() for i in range(n)])

population = popCreator(200)

#fitnessValues = list(map(oneMaxFitness, population))
fitnessValues = list(range(200))

for i in range(200):
    fitnessValues [i] = oneMaxFitness(population[i], a, b, c, d)


def cxOnePoint(child1, child2):
    s = random.randint(0, 2)
    child1[s:], child2[s:] = child2[s:], child1[s:]

def mutFlipBit(mutant, indpb=0.01):
    for indx in range(0,2):
        if random.random() < indpb:
            mutant[indx] = random.randint(-1000, 1000)
counter = 0
offspring =[]
while min(fitnessValues)!=0 or counter == 1000:
    counter +=1
    for n in range(200):
        offspring.clear()
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
          i1, i2, i3 = random.randint(0, 200-1), random.randint(0, 200-1), random.randint(0, 200-1)

        offspring.append(min([abs(oneMaxFitness(population[i1], a, b, c, d)) , abs(oneMaxFitness(population[i2], a, b, c, d)), abs(oneMaxFitness(population[i3], a, b, c, d))]))
    population = offspring

    for child1, child2 in zip(population[::2], population[1::2]):
        if random.random() < 0.9:
            cxOnePoint(child1, child2)

    for mutant in population:
        if random.random() < 0.1:
            mutFlipBit(mutant, indpb=1.0/3)
    FreshfitnessValues = list()
    for i in range(200):
        FreshfitnessValues[i] = oneMaxFitness(population[i], a, b, c, d)





    fitnessValues = FreshfitnessValues

print(population[1])


#print(population[1])

#print(fitnessValues[1])

