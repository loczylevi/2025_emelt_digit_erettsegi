
"""
1. Lista elemeinek négyzete
Írj egy programot, amely egy lista minden elemének a négyzetét kiszámítja
a map() és egy lambda függvény segítségével!

Példa bemenet:

python
Copy code
[1, 2, 3, 4]
Kimenet:

python
Copy code
[1, 4, 9, 16]
"""
lista = [1, 2, 3, 4]

lista2 = list(map(lambda num : num ** 2, lista))
print(list(map(lambda num : num ** 2, lista)))

"""
2. Páros számok szűrése
Szűrd ki egy listából a páros számokat
a filter() és egy lambda függvény segítségével!

Példa bemenet:

python
Copy code
[1, 2, 3, 4, 5, 6]
Kimenet:

python
Copy code
[2, 4, 6]
"""

vegyes = [1, 2, 3, 4, 5, 6]

paros = list(filter(lambda num : num % 2 == 0, vegyes))
print(list(filter(lambda num : num % 2 == 0, vegyes)))

"""

3. Lista elemeinek összeadása
Használd a reduce() függvényt, hogy kiszámítsd
egy lista elemeinek összegét! A reduce() a functools modulból importálható.

Példa bemenet:

python
Copy code
[1, 2, 3, 4]
Kimenet:

python
Copy code
10
"""
import functools
x = [1, 2, 3, 4]

#c = functools.reduce(lambda num : num + 1 ,x)

"""
4. Szavak hosszának kiszámítása
Írj egy programot, amely kiszámítja egy szavakból álló lista
minden szavának a hosszát a map() és egy lambda függvény segítségével!

Példa bemenet:

python
Copy code
["alma", "körte", "szilva"]
Kimenet:

python
Copy code
[4, 5, 6]
"""
szavak = ["alma", "körte", "szilva"]

szavak_hossza = list(map(lambda szo : len(szo), szavak))
print(list(map(lambda szo : len(szo), szavak)))

"""
5. Nagybetűvel kezdődő szavak szűrése
Szűrd ki azokat a szavakat egy listából, amelyek nagybetűvel kezdődnek, a filter() és egy lambda függvény segítségével!

Példa bemenet:

python
Copy code
["alma", "Banán", "cseresznye", "Dió"]
Kimenet:

python
Copy code
["Banán", "Dió"]
"""

szavak = ["alma", "Banán", "cseresznye", "Dió"]

nagybetusek = list(filter(lambda szo : szo[0].isupper(), szavak))

print(list(filter(lambda szo : szo[0].isupper(), szavak)))


"""
6. Lista rendezése hossz szerint
Rendezd egy szavakból álló listát a szavak hossza szerint növekvő sorrendben a sorted() és egy lambda függvény segítségével!

Példa bemenet:

python
Copy code
["alma", "banán", "cseresznye", "dió"]
Kimenet:

python
Copy code
["dió", "alma", "banán", "cseresznye"]
"""
szav = ["alma", "banán", "cseresznye", "dió"]

print(sorted(szav, key=lambda szo : len(szo)))
print(sorted(szav, key=len))

"""
7. Lista elemeinek szorzata
Számítsd ki egy lista elemeinek szorzatát a reduce() és egy lambda függvény segítségével!

Példa bemenet:

python
Copy code
[1, 2, 3, 4]
Kimenet:

python
Copy code
24
"""

szorzat = [1, 2, 3, 4]
#print(functools.reduce(lambda x:x,szorzat))

"""
8. Páros és páratlan számok különválasztása
Készíts egy programot, amely egy listát két részre oszt: páros számokra és páratlan számokra. Használj filter()-t és lambda függvényt!

Példa bemenet:

python
Copy code
[1, 2, 3, 4, 5, 6]
Kimenet:

python
Copy code
Páros számok: [2, 4, 6]
Páratlan számok: [1, 3, 5]
"""
gg = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda x : x % 2 == 0, gg)))
print(list(filter(lambda x : x % 2 != 0, gg)))


"""
9. Szavak listájának nagybetűssé alakítása
Használj map() és lambda függvényt, hogy minden szót nagybetűssé alakíts egy listában!

Példa bemenet:

python
Copy code
["alma", "körte", "szilva"]
Kimenet:

python
Copy code
["ALMA", "KÖRTE", "SZILVA"]
"""
szavak = ["alma", "körte", "szilva"]

print(list(map(lambda szo : szo.upper(),szavak)))

import functools
x = [1, 2, 3, 4]
eredmeny = functools.reduce(lambda a, b : a * b, x)
print(eredmeny)





