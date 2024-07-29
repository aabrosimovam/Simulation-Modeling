import random

def BRV():
    r=random.uniform(0.0,1.0)
    if r==0 or r==1:
        return BRV()
    else: return r


N=200
array=[0]*N
for i in range(N):
    array[i]=BRV()
    ##print(array[i])

k=20
lk=1/k
left_lk=0
right_lk=lk
Nj=[0]*k
j=0
while right_lk<=1:
    for i in range (N):
        if array[i]<right_lk and array[i]>left_lk:
            Nj[j]+=1
    j+=1
    left_lk=right_lk
    right_lk+=lk

X2=0.0
for i in range(k):
    X2=X2+((Nj[i]-(N/k))**2)
X2=X2*k/N

print("\nЧисло степеней свободы = ", k-1, "\nХи^2 = ", X2)
print("\nПри уровне значимости = 0,05 \nпо таблице критерия Пирсона пороговое значение статистики критерия = 30,1")
print("При уровне значимости = 0,01 \nпо таблице критерия Пирсона пороговое значение статистики критерия = 36,2")