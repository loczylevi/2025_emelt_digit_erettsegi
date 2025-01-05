#rendszám/óra/perc/sebesség

#(づ ◕‿◕ )づ


class Autok_mozgasa:
    def __init__(self,sor):
        rendszam,ora,perc,velocitas = sor.strip().split("\t")
        self.rendszam = rendszam
        self.ora = int(ora)
        self.perc = int(perc)
        self.velocitas = int(velocitas)
        
        
with open("jeladas.txt","r",encoding="UTF-8") as f:
    lista = [Autok_mozgasa(sor) for sor in f]
    
print(f"""2. feladat:
Az utolsó jeladás időpontja {lista[-1].ora}:{lista[-1].perc}, a jármű rendszáma {lista[-1].rendszam} """)

elso_rendszam = lista[0].rendszam


print(f"""3. feladat:
Az első jármű: {elso_rendszam}
Jeladásainak időpontjai: """, end="")

elso_jarmu = [(sor.ora,sor.perc) for sor in lista if elso_rendszam == sor.rendszam]

elso_jarmu2 = list(filter(lambda sor : elso_rendszam == sor.rendszam, lista))

#for sor in elso_jarmu2:
    #print(f"{sor.ora}:{sor.perc}",end=" ")
#print()

for sor in elso_jarmu:
    print(f"{sor[0]}:{sor[1]}",end=" ")
    
print()
"""
4. Kérje be a felhasználótól egy időpont óra és perc értékét, és adja meg, hogy hány jeladás
történt az adott időpontban! Ha nem történt jeladás, akkor 0-t írjon ki! 
"""
print("""4. feladat:""")


try:
    ora = int(input("Kérem, adja meg az órát: "))
    perc = int(input("Kérem, adja meg a percet: "))
    
    hany_jeladas = len([sor for sor in lista if sor.ora == ora and sor.perc == perc])

    hany_jeladas2 = len(list(filter(lambda sor : sor.ora == ora and sor.perc == perc, lista)))

    print(f"A jeladások száma: {hany_jeladas}")
    
except:
    print("Hiba számot kértem nem karakterláncot!")
    


print(f"""5. feladat:
A legnagyobb sebesség km/h: {max(lista, key=lambda sor : sor.velocitas).velocitas}
A járművek: """,end="")
[print(f"{sor.rendszam}",end=" ") for sor in lista if (max(lista, key=lambda sor : sor.velocitas).velocitas) == sor.velocitas]
    
print()

"""
6. Kérje be a felhasználótól egy jármű rendszámát, és jelenítse meg a jármű jeladásainak
időpontját és az adott rendszámú autó távolságát az útszakasz kezdetétől! A bevezető
példában az első jármű esetén a 6:04-kor a jármű távolsága az útszakasz kezdetétől 0,0 km,
míg 6:14-kor 15,8 km, mivel a jármű az eltelt 10 perc (10/60 óra) alatt 95 km/h-val haladt.
A kimenetet a mintának megfelelőn alakítsa ki, a távolságot minden esetben egy
tizedesjegyre kerekítve írja ki km mértékegységben! Ha nem szerepel a bekért rendszámmal
jármű, akkor azt egy rövid mondatban jelezze a felhasználónak!  
"""

bekeres = input("Kérem, adja meg a rendszámot: ")

szuro = [(sor.ora,sor.perc,sor.velocitas) for sor in lista if sor.rendszam == bekeres]


listacska =  []
for sor in szuro:
    listacska.append([sor[0],sor[1],sor[2],0])

def ido(ora,perc):
    return ora + (perc/60)

 
if len(szuro) > 0:
    for index in range(1,len(listacska)):
        t = ido(listacska[index][0], listacska[index][1]) - ido(listacska[index-1][0], listacska[index-1][1])
        v = listacska[index-1][2]
        s = v * t
        listacska[index][-1] += listacska[index - 1][-1] + s


print(*listacska, sep= "\n")
"""
7. Készítsen egy ido.txt szöveges állományt, amelynek mindegyik sorában egy-egy jármű
rendszáma, illetve első és utolsó jeladásának óra és perc értéke szerepeljen! Az állományban
minden jármű pontosan egyszer forduljon elő tetszőleges sorrendben! 
"""
kesz = []
ido_lista = []
index = 0
while index < len(lista)-1:
    rendszam = lista[index].rendszam
    legkisebb = min([(sor.ora,sor.perc) for sor in lista if sor.rendszam == rendszam])
    legnagyobb = max([(sor.ora,sor.perc) for sor in lista if sor.rendszam == rendszam])
    if rendszam not in kesz:
        kesz.append(rendszam)
        ido_lista.append([rendszam, legkisebb[0], legkisebb[1], legnagyobb[0], legnagyobb[1]])
    index = index + 1

with open("ido.txt","w",encoding="UTF-8") as f2:
    for sor in ido_lista:
        print(f"{sor[0]} {sor[1]} {sor[2]} {sor[3]} {sor[4]}",file=f2)

        











