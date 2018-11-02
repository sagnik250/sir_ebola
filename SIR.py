import numpy as np
import math


h = float(input("Enter time-step value"))
duration = float(input("Enter the duration of simulation"))
N = int(duration/h)

beta = float(input("Enter value of beta"))
gamma =  float(input("Enter value of gamma"))

population = np.zeros(3)

print("Enter initial population of susceptibles, infected, and recovered individuals respectively")

for i in range(3):
	
	population[i] = int(input(""))

def SIR():

	for i in range(N) :

		population[0] -= population[0] * population[1] * h * beta

		population[1] += (population[0] * population[1] * h * beta) - (population[1] * h * gamma)

		population[2] += population[1] * h * gamma

		print(i , population[0], population[1], population[2])

SIR()  
	
