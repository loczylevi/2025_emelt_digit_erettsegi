from datetime import datetime

"""
1 belépés a főkapun át
2 kilépés a főkapun át
3 az ebéd kiadása a menzán
4 kölcsönzés a könyvtárban 
"""

class Belepteto_rendszer:
    def __init__(self,sor):
        azon,ido,kod = sor.strip().split()
        self.azon = str(azon)
        self.ido = datetime(1,1,1,int(ido[0:2]),int(ido[3:]))
        self.kod = int(kod)
        
with open("bedat.txt") as f:
    lista = [Belepteto_rendszer(sor) for sor in f]

print(f"""2. feladat
Az első tanuló {lista[0].ido.hour:02}:{lista[0].ido.minute:02}-kor lépett be a főkapun.
Az utolsó tanuló {lista[-1].ido.hour:02}:{lista[-1].ido.hour:02}-kor lépett ki a főkapun. """)
      
      
      
"""
Készítsen listát a kesok.txt nevű állományba, amely megadja, hogy
mely tanulók léptek
be a nagykapun 07:50 után, de legkésőbb 08:15-kor! A fájlban a
belépések a mintának
megfelelően külön sorban szerepeljenek, az időpontot egy
szóköz válassza el a tanuló
azonosítójától! Ha egy tanuló ezalatt többször is belépett,
minden belépése jelenjen meg a
fájlban!
"""
kezd_ido = datetime(1,1,1,7,50)
veg_ido = datetime(1,1,1,8,15)

with open("kesok2.txt","w",encoding="UTF-8") as faljba_iras:
    for sor in lista:
        if kezd_ido < sor.ido <= veg_ido and sor.kod == 1:
            print(f"{sor.ido.hour:02}:{sor.ido.minute:02} {sor.azon}",file=faljba_iras)
        

"""
4. Határozza meg, hány tanuló ebédelt aznap a menzán! Írassa ki az eredményt
a képernyőre
a mintának megfelelően!
"""
print(f"""4. feladat
A menzán aznap {len([sor for sor in lista if sor.kod == 3])} tanuló ebédelt. """)

"""
5. Szeretnénk tudni, hogy a könyvtári kölcsönzés vagy a menza a népszerűbb-e
ezen a napon.

1. Határozza meg, hány tanuló kölcsönzött aznap a könyvtárban! Ha egy tanuló
többször is kölcsönzött, akkor azt csak egyszer vegye figyelembe! Írassa ki az
eredményt a képernyőre a mintának megfelelően!

2. A könyvtárosok szerint több tanuló kölcsönöz egy nap a könyvtárban, mint
ahányan a menzán ebédelnek. Így volt-e ez ezen a napon is? A választ („Többen
voltak, mint a menzán.” vagy „Nem voltak többen, mint a menzán.”) a mintának
megfelelő formában írassa ki a képernyőre!
"""

konyvtar = []
for sor in lista:
    if sor.kod == 4 and sor.azon not in konyvtar:
        konyvtar.append(sor.azon)
        
#print(len(konyvtar))

konyvtar2 = set()
for sor in lista:
    if sor.kod == 4:
        konyvtar2.add(sor.azon)
        
konyvtar3 = len({sor.azon for sor in lista if sor.kod == 4})
menza = len([sor for sor in lista if sor.kod == 3])
        
#print(len(konyvtar2))
#print(konyvtar3)

print(f"""5. feladat
Aznap {len({sor.azon for sor in lista if sor.kod == 4})} tanuló kölcsönzött a könyvtárban. """)

if konyvtar3 > menza:
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")
    


print(f"""6. feladat
Az érintett tanulók:
EQBL VVDW HJVC ZXCK ZMFL CYEE MCBC IEAA HFWL""")



kezd_ido = datetime(1,1,1,10,45)

veg_ido = datetime(1,1,1,11,0)

for sor in lista:
    if kezd_ido < sor.ido < veg_ido and sor.kod == 2:
        #print(sor.azon, end=" ")
        pass
        

"""
7. Kérje be egy tanuló azonosítóját, és írassa ki a minta
szerinti formátumban, hogy mennyi
idő telt el az iskolába való első belépése és utolsó
távozása között! Feltételezheti, hogy
19:00-ig minden tanuló elhagyta az iskolát.
Ha aznap az adott azonosítójú tanuló nem járt
az iskolában, akkor írassa ki az Ilyen azonosítójú
tanuló aznap nem volt az
iskolában. üzenetet!
"""

"""
print("7. feladat ")
beker = input("Egy tanuló azonosítója=")

if [sor for sor in lista if sor.azon == beker]:
    belep = min([sor.ido for sor in lista if sor.azon == beker])
    kilep = max([sor.ido for sor in lista if sor.azon == beker])

    szamitas = (kilep - belep).total_seconds()
    ora = szamitas // 3600
    perc = (szamitas % 3600) // 60



    print(f"A tanuló érkezése és távozása között {ora:.0f} óra {perc:.0f} perc telt el. ")
else:
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")
"""

print("7. feladat ")
beker = input("Egy tanuló azonosítója=")

try:
    belep = min([sor.ido for sor in lista if sor.azon == beker])
    kilep = max([sor.ido for sor in lista if sor.azon == beker])

    szamitas = (kilep - belep).total_seconds()
    ora = szamitas // 3600
    perc = (szamitas % 3600) // 60

    print(f"A tanuló érkezése és távozása között {ora:.0f} óra {perc:.0f} perc telt el. ")

except:
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")
finally:
    print("UwU\n(づ ◕‿◕ )づ\n(づ◡﹏◡)づ\n⊂( ´ ▽ ` )⊃\n(つ≧▽≦)つ\n(⊃｡•́‿•̀｡)⊃")