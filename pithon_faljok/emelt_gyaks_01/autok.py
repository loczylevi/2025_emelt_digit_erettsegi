#TLJ-509	6	4	95

class Autok:
    def __init__(self,sor):
        rendszam, ora,perc,velocitas = sor.strip().split("\t")
        self.rendszam = rendszam
        self.ora = int(ora)
        self.perc = int(perc)
        self.velocitas = int(velocitas)


with open("jeladas.txt","r",encoding="UTF-8") as f:
    lista = [Autok(sor) for sor in f]

print(f"""2. feladat:
Az utolsó jeladás időpontja {lista[-1].ora}:{lista[-1].perc}, a jármű rendszáma {lista[-1].rendszam} """)




elso_rendszam = lista[0].rendszam

idopontok = list(filter(lambda sor : sor.rendszam == elso_rendszam,lista))

idopontok2 = [[sor.ora,sor.perc] for sor in lista if sor.rendszam == elso_rendszam]

print(f"""3. feladat:
Az első jármű: {elso_rendszam}
Jeladásainak időpontjai:""",end=" ")
for sor in idopontok:
    print(f"{sor.ora}:{sor.perc}", end=" ")

print()


"""
4. Kérje be a felhasználótól egy időpont óra és perc értékét, és adja meg, hogy hány jeladás
történt az adott időpontban! Ha nem történt jeladás, akkor 0-t írjon ki! 
"""

print(f"""4. feladat:""")
bekeres_ora = int(input("Kérem, adja meg az órát: "))
bekeres_perc = int(input("Kérem, adja meg a percet: "))

szamlalo = len(list(filter(lambda sor : sor.ora == bekeres_ora and sor.perc == bekeres_perc, lista)))

szamlalo2 = len([sor for sor in lista if sor.ora == bekeres_ora and sor.perc == bekeres_perc])

print(f"A jeladások száma: {szamlalo} ")

"""
5. Állapítsa meg, hogy mennyi az adatok szerint a legnagyobb sebesség, amellyel egy jármű
a jeladáskor haladt, illetve adja meg az összes autó rendszámát, ami haladt ilyen sebességgel!
Amennyiben egy jármű többször is haladt a legnagyobb sebességgel, akkor a rendszámát
többször is megjelenítheti. A rendszámokat egy sorban, szóközzel elválasztva jelenítse meg
a minta szerint!
"""

legnagyobb = max(lista, key=lambda sor : sor.velocitas).velocitas

legnagyobb2 = max(map(lambda sor:sor.velocitas, lista))

leg_jarmuvek = list(filter(lambda sor:sor.velocitas == legnagyobb, lista))

print(f"""5. feladat:
A legnagyobb sebesség km/h: {legnagyobb2}""")
print(f"""A járművek: """,end = " ")
for sor in leg_jarmuvek:
    print(f"{sor.rendszam}",end=" ")

print()


"""
7. Készítsen egy ido.txt szöveges állományt, amelynek mindegyik sorában egy-egy jármű
rendszáma, illetve első és utolsó jeladásának óra és perc értéke szerepeljen! Az állományban
minden jármű pontosan egyszer forduljon elő tetszőleges sorrendben!
"""
#___________________________|||Példák|||______________________________________

#lista = [1,1,1,1,1,2,2,2,3,33,4,4,44,5,5,5,5,5,6,6,7,8,9,10]

#xs = set()

#for sor in lista:
#   xs.add(sor)
    
#xd = {sor for sor in lista}

#______________________________________________________________________________

"""
7. Készítsen egy ido.txt szöveges állományt, amelynek mindegyik sorában egy-egy jármű
rendszáma, illetve első és utolsó jeladásának óra és perc értéke szerepeljen! Az állományban
minden jármű pontosan egyszer forduljon elő tetszőleges sorrendben!
"""

uniq_rendszamok = {sor.rendszam for sor in lista}  # a setben nem lehet két azonos elem

with open("ido.txt","w", encoding="UTF-8") as f_write:
    for egyedi_rendszam in uniq_rendszamok:
        print(f"{egyedi_rendszam} {min([[sor.ora,sor.perc] for sor in lista if sor.rendszam == egyedi_rendszam])[0]} {min([[sor.ora,sor.perc] for sor in lista if sor.rendszam == egyedi_rendszam])[1]} {max([[sor.ora,sor.perc] for sor in lista if sor.rendszam == egyedi_rendszam])[0]} {max([[sor.ora,sor.perc] for sor in lista if sor.rendszam == egyedi_rendszam])[1]}", file=f_write)
