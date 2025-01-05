"""
1 belépés a főkapun át
2 kilépés a főkapun át
3 az ebéd kiadása a menzán
4 kölcsönzés a könyvtárban 
"""


class Belepteto:
    def __init__(self,sor):
        allomany,ido,kod = sor.strip().split(" ")
        self.allomany = allomany
        self.ido = ido
        self.kod = kod


with open("bedat.txt", "r", encoding="UTF-8") as f:
    lista = [Belepteto(sor) for sor in f]


print(f"""2. feladat
Az első tanuló {min([sor.ido for sor in lista])}-kor lépett be a főkapun.
Az utolsó tanuló {max([sor.ido for sor in lista])}-kor lépett ki a főkapun. """)

#print(max(lista, key=lambda sor : sor.ido).ido)

with open("kesok.txt", "w", encoding="UTF-8") as f2:
    kesok = []
    for sor in lista:
        if "07:50" < sor.ido < "08:15":
            kesok.append(sor)
    for sor2 in kesok: 
        #print(f"{sor2.ido} {sor2.allomany}",file=f2)
        f2.write(f"{sor2.ido} {sor2.allomany}\n")


menza = 0
for i in lista:
    if i.kod == "3":
        menza = menza + 1
        #menza += 1

print(f"""4. feladat
A menzán aznap {len([sor for sor in lista if sor.kod == "3"])} tanuló ebédelt. """)

#print(len(list(filter(lambda sor : "3" in sor.kod, lista))))


diakok = []

for sor in lista:
    if sor.kod == "4" and sor.allomany not in diakok:
        diakok.append(sor.allomany)

print(f"""5. feladat
Aznap {len(diakok)} tanuló kölcsönzött a könyvtárban.""")


"""
2. A könyvtárosok szerint több tanuló kölcsönöz egy nap a könyvtárban, mint
ahányan a menzán ebédelnek. Így volt-e ez ezen a napon is? A választ („Többen
voltak, mint a menzán.” vagy „Nem voltak többen, mint a menzán.”) a mintának
megfelelő formában írassa ki a képernyőre!
"""

menzasok = len([sor for sor in lista if sor.kod == "3"])

menzasok2 = len(list(filter(lambda sor : "3" in sor.kod,lista)))


if menzasok < len(diakok):
    print("""Többen voltak, mint a menzán.""")
else:
    print("""Nem voltak többen, mint a menzán.""")
    
"""
6. A portás reggel elfelejtette a hátsó kaput bezárni, ezért a 10:45-kor kezdődő szünetben
néhány tanuló kiment a hátsó kijáraton át a szemközti pékségbe tízórait venni. A portás csak
10:50-kor zárta be a hátsó kaput, így 10:50 után a korábban a hátsó kapun át távozott
tanulóknak a főbejáraton át kellett visszajönniük. Írassa ki a képernyőre egy-egy szóközzel
elválasztva ezeknek a tanulóknak az azonosítóját! (A szünet 11:00-ig tartott, és
feltételezheti, hogy azt megelőzően valamennyi érintett tanuló visszaért.) Vegye
figyelembe, hogy a tanulók egy része aznap csak 11:00-ra jött iskolába, illetve szabályosan
lépett ki!
"""

bemenet = [sor for sor in lista if sor.kod == "1" or sor.kod == "2"]

ido = [sor for sor in bemenet if sor.ido < "11:00"]


stat = dict()


for sor in ido:
    tanulo_kod = sor.allomany
    stat[tanulo_kod] = stat.get(tanulo_kod, 0 ) + 1
 
""" 
for sor, db in stat.items():
    print(sor,db)

"""
print("""6. feladat
Az érintett tanulók:""")
[print(f"{sor}" ,end=" ") for sor,db in stat.items() if db == 2]

print()
"""
7. Kérje be egy tanuló azonosítóját, és írassa ki a minta szerinti formátumban, hogy mennyi
idő telt el az iskolába való első belépése és utolsó távozása között! Feltételezheti, hogy
19:00-ig minden tanuló elhagyta az iskolát. Ha aznap az adott azonosítójú tanuló nem járt
az iskolában, akkor írassa ki az Ilyen azonosítójú tanuló aznap nem volt az
iskolában. üzenetet!
"""


print(f"""7. feladat""")

bekeres = input("Egy tanuló azonosítója=")

szures = [sor.ido for sor in lista if sor.allomany == bekeres]

print(szures)



def erkezes_tavozas_differenciaja(ora, perc):
    return (int(ora)*60) + int(perc)





#ora = kilep[0:2] - belep[0:2]

if len(szures) > 0:
    belep = min(szures)
    kilep = max(szures)
    osszesen = erkezes_tavozas_differenciaja(int(kilep[:2]), int(kilep[3:])) - erkezes_tavozas_differenciaja(int(belep[:2]), int(belep[3:]))
    ora = osszesen / 60
    perc = osszesen % 60
    print(f"""A tanuló érkezése és távozása között {osszesen/60:.0f} óra {perc} perc telt el. """)
else:
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")





