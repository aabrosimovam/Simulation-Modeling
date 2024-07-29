import random
# from scipy.integrate import quad

def F(x):
    return (((x * (2 ** (7 / 4) - 1) + 1) ** (4 / 7) - 1))
# def pm(x):
#     return (x * (7 * ((x + 1) ** (3 / 4))) / (4 * (2 ** (7 / 4) - 1)))
# def pd(x):
#     m = Integral_m()
#     return ((x - m) ** 2 * (7 * ((x + 1) ** (3 / 4))) / (4 * (2 ** (7 / 4) - 1)))

def BRV():
    r=random.uniform(0.0,1.0)
    if r==0 or r==1:
        return BRV()
    else: return r

def CRV():
    r = BRV()
    return F(r)

# def Integral_m():
#     result = quad(pm, 0, 1)[0]
#     return result

# def Integral_d():
#     result = quad(pd, 0, 1)[0]
#     return result


N = 100000
f = [0] * N
sum_m = 0; sum_d = 0

for i in range (N):
    f[i] = CRV()
    sum_m += f[i]
sum_m = sum_m / N

for i in range (N):
    sum_d += (f[i] - sum_m) ** 2
sum_d = sum_d / (N - 1)

m = 0.54196381738
d = 0.08133465079

# m = Integral_m()
# d = Integral_d()

print("Теоретическое мат.ожидание: ", m)
print("Теоретическая дисперсия: ", d)
print("Выборочное среднее: ", sum_m)
print("Несмещенная выборочная дисперсия: ", sum_d)

print ("\nОценка качества мат. ожидания: ", (abs(m - sum_m) / m) * 100, "% ")
print ("Оценка качества дисперсии: ", (abs(d - sum_d) / d) * 100, "% ")