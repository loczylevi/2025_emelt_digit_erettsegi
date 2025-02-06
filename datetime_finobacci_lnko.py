import random

szam1 = 252

szam2 = 105

lnko = set()

for oszto in range(1,szam1):
    if szam1 % oszto == 0 and szam2 % oszto == 0:
        lnko.add(oszto)
        
print(max(lnko))


def lnko(a, b):
    while b:
        a, b = b, a % b
    return a

szam1 = 252
szam2 = 105

print(lnko(szam1, szam2))  # 5
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def finobacci(c):
    lista = [0,1]
    szam = 0
    while len(lista) < c:
        osszeado = lista[szam] + lista[szam+1]
        lista.append(osszeado)
        szam = szam + 1

    return lista

print(finobacci(10))

def fibonacci(c):
    lista = [0, 1]  # Kezdő Fibonacci számok

    while len(lista) < c:  # Amíg nincs elég elem a listában
        osszeado = lista[-1] + lista[-2]  # Az utolsó két elem összege
        lista.append(osszeado)  # Hozzáadjuk a listához

    return lista  # Visszaadjuk az első 'c' Fibonacci számot

print(fibonacci(10))  # [0, 1, 1, 2, 3]


def fibonacci_rekurziv(n):
    if n == 0:  # Alap eset
        return 0
    elif n == 1:  # Alap eset
        return 1
    else:
        return fibonacci_rekurziv(n - 1) + fibonacci_rekurziv(n - 2)  # Rekurzív hívás

# Példa futtatás
print(fibonacci_rekurziv(0))   # 5
print(fibonacci_rekurziv(10))  # 55
 

from datetime import datetime

kezd = datetime(1,1,1,7,50)
veg = datetime(1,1,1,10,40)

koztes = datetime(1,1,1,8,54)
if kezd < koztes < veg:
    print(f"{kezd.hour:02}:{kezd.minute:02},{koztes.hour:02}:{koztes.minute:02},{veg.hour:02}:{veg.minute:02}")








