#CEFX 07:00 1
#OELK 07:00 1

#1 --> belép
#2 --> kilép
#3 --> menza zaba
#4 --> book rent

class Belepteto_rendszer:
    def __init__(self,sor):
        azon,ido,kod = sor.strip().split()
        self.azon = azon
        self.ido = ido
        self.kod = int(kod)

with open("bedat.txt","r",encoding="UTF-8") as f:
    lista = [Belepteto_rendszer(sor) for sor in f]




print(f"""2. feladat
Az első tanuló {lista[0].ido}-kor lépett be a főkapun.
Az utolsó tanuló {lista[-1].ido}-kor lépett ki a főkapun. """)


with open("kesok.txt","w",encoding="UTF-8") as faljba_iras:
    for sor in lista:
        if "07:50" < sor.ido and sor.ido < "08:15" and sor.kod == 1:
                print(f"{sor.ido} {sor.azon}", file=faljba_iras)


print(f"""4. feladat
A menzán aznap {len([sor for sor in lista if sor.kod == 3])} tanuló ebédelt. """)


konyvtar = len({sor.azon for sor in lista if sor.kod == 4})

menza = len([sor for sor in lista if sor.kod == 3])

print(f"""5. feladat
Aznap {konyvtar} tanuló kölcsönzött a könyvtárban""")

if konyvtar < menza:
     print("Nem voltak többen, mint a menzán")
else:
     print("Többen voltak, mint a menzán.")
     

hatso_kapu = [sor.azon for sor in lista if "10:50" < sor.ido and sor.ido < "11:00" and sor.kod == 1]

print(f"""6. feladat
Az érintett tanulók:
{' '.join(map(str,hatso_kapu))} """)

print("7. feladat ")
bekeres = input("Egy tanuló azonosítója=")


def ido_szamito(t2,t):
    try:

        ora = int(t[:2])
        perc = int(t[3:])

        ora2 = int(t2[:2])
        perc2 = int(t2[3:])  

        percek = (ora * 60) + perc
        percek2 = (ora2 * 60) + perc2

        return percek2 - percek
    
    except:
         print("index hiba :3")




if len([sor for sor in lista if sor.azon == bekeres]) > 1:
    belepes = min([sor.ido for sor in lista if sor.azon == bekeres])
    kilepes = max([sor.ido for sor in lista if sor.azon == bekeres])
    szamitas = (ido_szamito(kilepes,belepes))
    print(f"A tanuló érkezése és távozása között {szamitas // 60} óra {szamitas % 60} perc telt el. ")
else:
     print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")




