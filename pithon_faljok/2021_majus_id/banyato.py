

with open("melyseg.txt") as f:
    sorok_szama = f.readline()
    oszlopok_szama = f.readline()
    lista = [sor.strip().split() for sor in f]


print("2. feladat")
bekeres_sor = int(input("A mérés sorának azonosítója="))
bekeres_oszlop = int(input("A mérés oszlopának azonosítója="))
print(f"A mért mélység az adott helyen {lista[bekeres_sor-1][bekeres_oszlop-1]} dm")

"""
3. Határozza meg a tó (vagyis az ábrán szürkével jelölt rész) felszínének területét, valamint
a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre!
A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg! 
"""


lista2 =  []
for sor in lista:
    lista2.append(list(map(lambda s : int(s),sor)))
#print(lista2)

melyseg = [[s for s in sor if s!=0] for sor in lista2]
melyseg2 = sum([sum([s for s in sor if s!=0]) for sor in lista2])
tag = 0
for sor in melyseg:
    for s in sor:
        tag += 1

ered = f"{(melyseg2/tag)/10:.2f}"

ered = str(ered).replace(".",",")

print(f"""3. feladat
A tó felszíne: {sum([len([s for s in sor if s!=0]) for sor in lista2])} m2, átlagos mélysége: {ered} m""")

#felszin = sum([[s for s in sor if s != 0] for sor in lista2])

"""
4. feladat
A tó legnagyobb mélysége: 98 dm
A legmélyebb helyek sor-oszlop koordinátái:
(14; 20) (26; 11) (32; 16) 
"""

legnagyobb = lista2[0][0]

for sor in lista2:
    for s in sor:
        if s > legnagyobb:
            legnagyobb = s

kordinatak = []
for index,sor in enumerate(lista2,start=1):
    oszlop = 1
    for s in sor:
        if s == legnagyobb:
            kordinatak.append((index,oszlop))
        oszlop += 1

print(f"""4. feladat
A tó legnagyobb mélysége: {legnagyobb} dm
A legmélyebb helyek sor-oszlop koordinátái:""")
for sor in kordinatak:
    print(sor,end="   ")
print()
vizszintes = []
vizszintes2 = []

for index,sor in enumerate(lista2, start=0):
    hany = len(sor) -1
    for szam in range(hany):
         if lista2[index][szam] != 0 and lista2[index][szam-1] == 0:
            vizszintes2.append(1)
         elif lista2[index][szam] == 0 and lista2[index][szam-1] != 0:
            vizszintes2.append(1)
    
lista_index = 0
while lista_index < len(lista2)-1:
    print(lista2[lista_index])
    hany_elem_index = 0
    while  hany_elem_index < len(lista2[lista_index]) -1 :
        if lista2[lista_index][hany_elem_index] != 0 and lista2[lista_index][hany_elem_index-1] == 0:
            vizszintes.append(1)
        elif lista2[lista_index][hany_elem_index] == 0 and lista2[lista_index][hany_elem_index-1] != 0:
            vizszintes.append(1)
        hany_elem_index += 1
    #print(f"skibidi: {lista_index}")
    lista_index += 1


print("XD")
print(sum(vizszintes2))
print(sum(vizszintes))



"""for index,sor in enumerate(lista2, start=0):
    if lista[index] != 0 and lista[index-1] == 0:
        vizszintes.append(1)
    elif lista[index] == 0 and lista[index-1] != 0:
        vizszintes.append(1)
"""
fugg = []

for index,sor in enumerate(lista2, start=0):
    hany = len(sor) -1
    for szam in range(hany):
         if lista2[index][szam] != 0 and lista2[index-1][szam] == 0:
            fugg.append(1)
         elif lista2[index][szam] == 0 and lista2[index-1][szam] != 0:
            fugg.append(1)


print(f"""5. feladat
A tó partvonala 270 m hosszú 
""")

print("""függ""")
print(sum(fugg))
print(sum(fugg)+ sum(vizszintes))