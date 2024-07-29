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
    t = [(- 1 / lmbd) * log(a)] 
    while t[-1] < T:
        t.append(t[-1] + random_poisson(lmbd))
    return t[:-1] 
    

def mix_stream(stream1, stream2):
    mixed_stream = []
    mixed_stream.extend(stream1)
    mixed_stream.extend(stream2)
    mixed_stream.sort()
    return mixed_stream


def gamma_estimation(T, lambda1, lambda2, N):
    # оценка параметра потока
    gamma = 0
    for i in range(N):
        stream1 = form_stream(T, lambda1)
        stream2 = form_stream(T, lambda2)
        t = mix_stream(stream1, stream2)
        events = len(t)
        gamma += events / T
    return gamma / N

lambda1 = 0.3
lambda2 = 0.7
N = 10000
T = 10

gamma = gamma_estimation(T, lambda1, lambda2, N)

print("Оценка параметра потока гамма: ", gamma)
print("Оценка: ", abs((gamma - (lambda1 + lambda2)) / (lambda1 + lambda2)) * 100, "%")
