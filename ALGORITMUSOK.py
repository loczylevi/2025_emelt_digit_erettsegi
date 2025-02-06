"""1. Kiválogatás (Filtering)
Írj egy programot, amely egy listában szereplő számokat
csak a páros számokra szűri le.
"""
import random
meddig = random.randint(1,10)
lista = []
for szam in range(0,meddig):
    lista.append(szam)
    
import random
meddig2 = random.randint(1,10)
lista2 = []
for szam in range(0,meddig2):
    lista2.append(szam)
    
print(lista)
print(lista2)
print("Páros számok:", end=" ")
paros_szamok = [print(f"{szam}", end=", ") for szam in lista if szam % 2 == 0]

print()
"""
2. Rendezés (Sorting)
Írj egy programot, amely egy lista számokat növekvő sorrendbe rendez.
"""

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):  # Ennyiszer kell végigmenni a listán
        for j in range(n - 1 - i):  # Az utolsó i elem már a helyén van
            if numbers[j] > numbers[j + 1]:  # Ha rossz sorrendben vannak
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Cseréljük őket
    return numbers

# Teszteljük
numbers = [5, 3, 8, 1, 2]
print(bubble_sort(numbers))  # [1, 2, 3, 5, 8]




"""
3. Szétválogatás (Partitioning)
Írj egy programot, amely egy listát két részre oszt, ahol
az első lista tartalmazza a kisebb vagy egyenlő értékeket egy adott számhoz képest, a második lista pedig a nagyobb értékeket.
"""
print("\n\n")
adott_szam = random.randint(2, 5)
kiseb_szamok = []
nagyobb_szamok = []
for szam in lista:
    if szam > adott_szam:
        nagyobb_szamok.append(szam)
    elif szam <= adott_szam:
        kiseb_szamok.append(szam)
        
print(f"Adott szám: {adott_szam}\nkisebb számok {kiseb_szamok}\nnagyobb szamok: {nagyobb_szamok}")
        




"""
4. Metszet (Intersection)
Írj egy programot, amely két lista közötti metszetet adja vissza.
"""
metszett = []
for sor in lista:
    for szam in lista2:
        if sor == szam:
            metszett.append(sor)
            
print(lista)
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")
print(lista2)
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")
print(metszett)
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")
"""
5. Unió (Union)
Írj egy programot, amely két lista unióját adja vissza, azaz
egyesíti a két listát, eltávolítva a duplikált elemeket.
"""
print(f"Egyik lista: {lista}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")
print(f"Másik lista: {lista2}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")


unio = set()
for sor in lista:
    for szam in lista2:
            unio.add(sor)
            unio.add(szam)

print(f"Únió: {lista}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")


unio2 = []
for sor in lista:
    for szam in lista2:
        if sor not in unio2:
            unio2.append(sor)
        if szam not in unio2:
            unio2.append(szam)
        
    
print(f"Únió2: {lista}")
print("::::::::::::::::::::::::::::::::::::::::::::::::::...")


"""
6. Rendezett Unió
Írj egy programot, amely a két lista unióját úgy adja vissza,
hogy az eredmény rendezett legyen.
"""

def rendezes(c):
    n = len(c)
    for i in range(n-1):
        for j in range(n - 1 - i):
             if c[j] > c[j + 1]:  # Ha rossz sorrendben vannak
                c[j], c[j + 1] = c[j + 1], c[j]
    return c
print(rendezes(unio2))


"""
7. Szűrés és Rendezés
Írj egy programot, amely egy listában szereplő számokat csak
a pozitív számokra szűri le, majd rendezi őket növekvő sorrendbe.
"""
unio3 = list(set(lista) | set(lista2))
# metszet
print(list(set(lista) & set(lista2)))
# unio
print(list(set(lista) | set(lista2)))
# különbség
print(list(set(lista) - set(lista2)))

"""
Ezeket a feladatokat próbálhatod megoldani, hogy gyakorold
a kiválogatás, rendezés, szétválogatás, metszet és unió típusú
algoritmusokat. Ha bármelyik feladathoz segítségre van szükséged,
csak szólj!
"""
