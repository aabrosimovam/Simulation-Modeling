import random
from math import log

def BRV():
    r=random.uniform(0.0,1.0)
    if r==0 or r==1:
        return BRV()
    else: return r

def poisson(lmbd):
    a = BRV()
    return - 1 / lmbd * log(a)

def run_simulation(lmbd, mu, T):
    t1 = poisson(lmbd) 
    t2 = poisson(mu)
    count = 0
    loss_count = 0
    while t1 <= T:
        count += 1
        if t1 > t2:
            t2 = t1 + poisson(mu)
        else:
            loss_count += 1
        t1 += poisson(lmbd)
    return loss_count / count

lmbd = 2
mu = 1
T = 10000

theoretical = lmbd / (lmbd + mu)

result = run_simulation(lmbd, mu, T)

print("Вероятность потери заявки: ", result)
print("Теоретическая вероятность: ", theoretical)
print("Разница: ", abs(theoretical - result) / theoretical * 100, "%")