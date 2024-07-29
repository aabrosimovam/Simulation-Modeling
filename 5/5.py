import random
from math import log

def BRV():
    r=random.uniform(0.0,1.0)
    if r==0 or r==1:
        return BRV()
    else: return r

def random_poisson(lmbd):
    a = BRV()
    return - 1 / lmbd * log(a)
        
def form_stream(T, lmbd):
    a = BRV()
    t = - 1 / lmbd * log(a)
    count = 0
    while t < T:
        t += random_poisson(lmbd)
        count += 1
    return count

def gamma_estimation(T, lambda1, lambda2, N):
    # оценка параметра потока
    gamma = 0
    for i in range (N):
        stream1 = form_stream(T,lambda1)
        stream2 = form_stream(T,lambda2)
        gamma += (stream1 + stream2) / T
    return gamma / N


lambda1 = 10
lambda2 = 10
N = 10000
T = 100

gamma = gamma_estimation(T, lambda1, lambda2, N)

print("Оценка параметра потока гамма: ", gamma)
print("Оценка: ", abs((gamma - (lambda1 + lambda2)) / (lambda1 + lambda2)) * 100, "%")
