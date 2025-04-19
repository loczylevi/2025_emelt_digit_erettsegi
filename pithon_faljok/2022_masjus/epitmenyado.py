#adószáma, utca nevünk, házszám, adósáv, terulet

class Epitmenyado:
    def __init__(self,sor):
        adoszam,utca,hazszam,adosav,terulet = sor.strip().split()
        self.adoszam = int(adoszam)
        self.utca = str(utca)
        self.hazszam = str(hazszam)
        self.adosav = str(adosav)
        self.terulet = int(terulet)

with open("utca.txt","r",encoding="UTF-8") as f:
    elso_sor = f.readline()
    masodik_sor= f.readline()
    lista = [Epitmenyado(sor) for sor in f]

print(f"""2. feladat. A mintában {len(lista)} telek szerepel. """)

bekeres = int(input("3. feladat. Egy tulajdonos adószáma: "))

kereso_ado = [sor for sor in lista if sor.adoszam == bekeres]

if len(kereso_ado) > 0:
    for sor in kereso_ado:
        print(f"{sor.utca} utca {sor.hazszam}")
else:
    print(f"„Nem szerepel az adatállományban.”")

szeletelo = masodik_sor.split()
arak = [int(sor) for sor in szeletelo]

def ado(sav,alap):
    if sav == "A":
        return arak[0] * alap
    if sav == "B":
        return arak[1] * alap
    if sav == "C":
        return arak[2] * alap
    
ossz = 0
for sor in lista:
    if sor.adosav == "A":
        ossz += ado(sor.adosav,sor.terulet)
        
a_xd = sum([ado(sor.adosav,sor.terulet) for sor in lista if sor.adosav == "A"])
b_xd = sum([ado(sor.adosav,sor.terulet) for sor in lista if sor.adosav == "B"])
c_xd = sum([ado(sor.adosav,sor.terulet) for sor in lista if sor.adosav == "C"])

ossz_c = 0
for sor in lista:
    if sor.adosav == "C" and ado(sor.adosav,sor.terulet) > 10000:
        ossz_c += ado(sor.adosav,sor.terulet)
    else:
        ossz_c = 0
        break

print(f"""5. feladat
A sávba {len([sor for sor in lista if sor.adosav == "A"])} telek esik, az adó {sum([ado(sor.adosav,sor.terulet) for sor in lista if sor.adosav == "A"])} Ft.
B sávba {len([sor for sor in lista if sor.adosav == "B"])} telek esik, az adó {sum([ado(sor.adosav,sor.terulet) for sor in lista if sor.adosav == "B"])} Ft.
C sávba {len([sor for sor in lista if sor.adosav == "C"])} telek esik, az adó {sum([ado(sor.adosav,sor.terulet) for sor in lista if sor.adosav == "C"])} Ft. """)
    
unique_id = set()

for sor in lista:
    unique_id.add(sor.adoszam)
    
lista2 = []
for sor in lista:
    for sor2 in unique_id:
        if sor.adoszam == sor2:
            lista2.append([sor2,ado(sor.adosav,sor.terulet),sor.adosav,sor.terulet])
 
print(lista2)
with open("fizetendo.txt","w",encoding="UTF-8") as f2:
    for sor in lista2:
        if ado(sor[2],sor[3]) > 10000:
            print(f"{sor[0]} {ado(sor[2],sor[3])}",file=f2)
        else:
            print(f"{sor[0]} 0",file=f2)