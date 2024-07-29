import random
import numpy as np
from sympy import symbols, solve, Eq
        
def BRV():
    r=random.uniform(0.0,1.0)
    if r==0 or r==1:
        return BRV()
    else: return r

def DRV(probability):
    r = BRV()
    count = 0
    while r > 0:
        r -= probability[count]
        if r <= 0:
            return count
        count += 1           

def First_Geometric_Interpretation(a):
    d1 = symbols('d1')
    p1 = symbols('p1')

    equationd = Eq(d1 * (a[0][0] - a[1][0]) + a[1][0], d1 * (a[0][1] - a[1][1]) + a[1][1])
    solutiond = np.float_(solve(equationd,d1))

    v = np.float_(solutiond * (a[0][0] - a[1][0]) + a[1][0])
    
    equationp = Eq(a[0][0] * p1 + a[0][1] * (1 - p1), v)
    solutionp = np.float_(solve(equationp))

    # print ("d1 = ", solutiond)
    # print ("d2 = ", 1-solutiond)
    # print ("p1 = ", solutionp)
    # print ("p2 = ", 1-solutionp)
    # print ("Цена игры v = ", v)

    return v, [np.float_(solutiond),np.float_(1-solutiond)], [np.float_(solutionp),np.float_(1-solutionp)]

def First_Player_Wins(strategy1, strategy2, a, N):
    win = 0
    for _ in range (N):
        i = DRV(strategy1)
        j = DRV(strategy2)
        win += a[i][j]
    return win / N


a = [[8,-3],[-1,5]]
v, strategy1, strategy2 = First_Geometric_Interpretation(a)

print("Первый:", strategy1)
print("Второй:", strategy2)
print ("Цена игры v = ", v)

N=10000
print("Средний выигрыш первого игрока: ", First_Player_Wins(strategy1, strategy2, a, N))




