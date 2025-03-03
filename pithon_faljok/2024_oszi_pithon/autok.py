# TLJ-509	6	4	95



class Autok:
    def __init__(self,sor):
        rendszam, ora, perc, km_h = sor.strip().split("\t")
        self.rendszam = rendszam 
        self.ora = int(ora)
        self.perc = int(perc)
        self.km_h = int(km_h)



with open("jeladas.txt") as f:
    #lista = [sor.strip().split("\t") for sor in f]
    lista = [Autok(sor) for sor in f]




print(f"""2. feladat:
Az utolsó jeladás időpontja {lista[-1].ora}:{lista[-1].perc}, a jármű rendszáma {lista[-1].rendszam} """)

elso_jarmu = lista[0].rendszam

elso_jarmu_adatai = [[sor.ora,sor.perc] for sor in lista if sor.rendszam == elso_jarmu]

print(f"""3. feladat:
Az első jármű: {elso_jarmu}""")

print("Jeladásainak időpontjai: ",end="")
for ido in elso_jarmu_adatai:
    print(f"{ido[0]}:{ido[1]} ",end="")

print()

print("""4. feladat:""")

beker_ora = int(input("Kérem, adja meg az órát: "))
                
beker_perc = int(input("Kérem, adja meg a percet: "))

idopont_kereso = len([1 for sor in lista if sor.ora == beker_ora and sor.perc == beker_perc])

print(f"""A jeladások száma: {idopont_kereso} """)

legnagyobb_jarmuvek = [sor.rendszam for sor in lista if sor.km_h == max(lista, key=lambda sor : sor.km_h).km_h]

print(f"""5. feladat:
A legnagyobb sebesség km/h: {max(lista, key=lambda sor : sor.km_h).km_h} 
A járművek: {' '.join(map(str,legnagyobb_jarmuvek))}""")

#print(list(map(lambda sor : str(sor) , legnagyobb_jarmuvek)))

"""
for sor in legnagyobb_jarmuvek:
    print(f"{sor} ",end="")
print()
"""

print("6. feladat:")

bekert_rendszam = input("Kérem, adja meg a rendszámot: ")

hola_kocsi = [0]
"""
for index in range(0,len(lista)-1):
    ido_nagyobbik_ora = lista[index+1].ora * 60
    ido_nagyobbik_perc = lista[index+1] 
    t_nagy = ido_nagyobbik_perc + ido_nagyobbik_ora

    ido_kisebb_ora = lista[index].ora * 60
    ido_kisebb_perc = lista[index] 
    t_kicsi = ido_kisebb_ora + ido_kisebb_perc

    t_szamitas = t_nagy - t_kicsi
    tav = 
"""




"""
Készítsen egy ido.txt szöveges állományt, amelynek mindegyik sorában
egy-egy jármű
rendszáma, illetve első és utolsó jeladásának óra és perc értéke 
szerepeljen! Az állományban
minden jármű pontosan egyszer forduljon elő tetszőleges sorrendben! 
"""
halmaz = set()

for sor in lista:
    halmaz.add(sor.rendszam)

adatok = []
for rend in halmaz:
    x_idok = [[sor.ora,sor.perc] for sor in lista if sor.rendszam == rend]
    adatok.append([rend,min(x_idok), max(x_idok)])

adatok.sort(key=lambda sor : sor[0]) # jajj de goofy sor egyem a zuzáját

with open("ido.txt","w",encoding="UTF-8") as faljba_iras:
    for sor in adatok:
        print(f"{sor[0]} {sor[1][0]} {sor[1][1]} {sor[2][0]} {sor[2][1]}", file=faljba_iras)


