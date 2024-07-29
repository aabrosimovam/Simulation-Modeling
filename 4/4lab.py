import random
import numpy as np
import matplotlib.pyplot as plt

def BRV():
    r=random.uniform(0.0,1.0)
    if r==0 or r==1:
        return BRV()
    else: return r

def NRV(M, D):
    sum = 0
    n = 12
    for _ in range (n):
        r = BRV()
        sum += r
    result = (sum - n/2) * ((12/n) ** (1/2))
    return result * (D**(1/2)) + M

def threesigmamethod(array, N, M, D):
    sum = 0
    for i in range(N):
        if (array[i] > M - 3 * D**(1/2) and array[i] < M + 3 * D**(1/2)):
            sum += 1
    if (sum / N >= 0.9973):
        print ("Правило трех сигм выполняется:", sum / N, ">= 0.9973")
    else: 
        print ("Правило трех сигм не выполняется:", sum / N, " < 0.9973")

def barchart(array, min, max):
    step = 0.001
    bar = np.arange(min, max+step, step)

    frequence = [0] * int(((max+step-min)//step))
    for i in range (len(array)):
        j = 1
        while (bar[j] <= array[i]): 
            j += 1
        frequence[j-1] += 1

    plt.bar(bar[:-1], frequence, step, align='center')
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.title('Гистограмма с заданным шагом')

    plt.show()

M = 1/2
D = 1/12
N = 10000
array = [None] * N

array[0] = NRV(M, D)
min = array[0]; max = array[0]

for i in range(1,N):
    array[i] = NRV(M, D)
    if (max < array[i]): max = array[i]
    if (min > array[i]): min = array[i]

threesigmamethod(array, N, M, D)
barchart(array, min, max)
