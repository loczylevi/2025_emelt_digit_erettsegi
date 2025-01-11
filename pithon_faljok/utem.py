#6	26	7	10	GIOSY	foci

class Tabor:
    def __init__(self,sor):
        kezd_ho,kezd_na,veg_ho,veg_na, diakok, tabor = sor.strip().split("\t")
        self.kezd_ho = int(kezd_ho)
        self.kezd_na = int(kezd_na)
        self.veg_ho = int(veg_ho)
        self.veg_na = int(veg_na)
        self.diakok = str(diakok)
        self.tabor = str(tabor)
        
with open("taborok.txt") as f:
    taborok = [Tabor(sor) for sor in f]
    
print(f"""2. feladat
Az adatsorok száma: {len(taborok)}
Az először rögzített tábor témája: {taborok[0].tabor}
Az utoljára rögzített tábor témája: {taborok[-1].tabor}""")


"""3. Írja a képernyőre, mikor kezdődik a „zenei” tábor! Ha több ilyen tábor is volt,
az összeset jelenítse meg a lenti mintának megfelelően! Ha egy sem volt, akkor a „Nem
volt zenei tábor.” szöveget jelenítse meg a képernyőn!"""


zenei_tabor = [(sor.kezd_ho,sor.kezd_na) for sor in taborok if sor.tabor == "zenei"]

if len(zenei_tabor):
    print("3. feladat")
    for sor in zenei_tabor:
        print(f"Zenei tábor kezdődik {sor[0]}. hó {sor[1]}. napján. ")
        
else:
    print("Nem volt zenei tábor")
    

"""4. Keresse meg, melyik táborba jelentkeztek a legtöbben! Írja a képernyőre a tábor kezdő
dátumát és a témáját! Ha több ilyen tábor is van, az összeset jelenítse meg!"""

legnagyobbak = []
max_resztvevo = 0

for sor in taborok:
    if len(sor.diakok) > max_resztvevo:
        max_resztvevo = len(sor.diakok)
        legnagyobbak = []
    if len(sor.diakok) == max_resztvevo:
        legnagyobbak.append([sor.kezd_ho,sor.kezd_na,sor.tabor])
        


print(f"""4. feladat
Legnépszerűbbek:""")
for big in legnagyobbak:
    print(*big,sep=" ")
    


"""5. Készítsen függvényt sorszam néven, amely megadja, hogy a paraméterként kapott
hónap és nap a nyári szünet hányadik napja! A dátumot a függvény két egész számként
kapja meg, a visszaadott érték egy egész szám legyen! A nyári szünet első napja június
(6. hó) 16. A nyári szünet 77. napja augusztus (8. hó) 31. (A nyári hónapok rendre 30,
31, 31 naposak.) A későbbi feladatok megoldásánál ezt a függvényt felhasználhatja. """

def sorszam(honap,nap):
    honapok = [14, 31, 31]
    kics_ho = 6
    kics_na = 16
    nagy_ho = 8
    nagy_na = 31
    hanyadik_nap = 0
    for ho in honapok:
        if honap == ho:
            hanyadik_nap += ho
            
    return hanyadik_nap + nap


            
"""
7. Olvassa be egy tanuló betűjelét! Határozza meg, hogy az adott betűjelű tanuló mely
táborok iránt érdeklődött! A táborok adatait kezdő dátum szerint növekvő sorrendben
írja az egytanulo.txt fájlba a minta formátumának megfelelően! Jelenítse meg
a képernyőn, hogy a tanuló mindegyiken részt tud-e venni, azaz nincs-e olyan nap,
amelyen több táborban kellene lennie! """

print("""7. feladat""")
bekeres = input("Adja meg egy tanuló betűjelét: ")

kereso = [([(sor.kezd_ho,sor.kezd_na),sor.veg_ho,sor.veg_na, sor.tabor]) for sor in taborok if bekeres in sor.diakok]

kereso.sort(key= lambda sor : sor[0])


with open("egytanulo.txt", "w") as f2:
    for sor in kereso:
        print(f"{sor[0][0]}.{sor[0][1]}-{sor[1]}.{sor[2]}. {sor[3]}",file=f2)





        
        
        