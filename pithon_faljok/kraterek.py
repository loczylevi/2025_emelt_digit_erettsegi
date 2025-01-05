

#5.23	2.47	3.86	George Ogden Abell

class Krater:
    def __init__(self,sor):
        x,y,radius,nev = sor.strip().split("\t")
        self.x = float(x)
        self.y = float(y)
        self.radius = float(radius)
        self.nev = str(nev)

with open("felszin_tpont.txt") as f:
    kraterek = [Krater(sor) for sor in f]

print(f"""2. feladat
A kráterek száma: {len(kraterek)} """)

print(f"""3. feladat""")

bekeres = input("Kérem egy kráter nevét: ")

kereso = [sor for sor in kraterek if bekeres in sor.nev]
kereso2 = list(filter(lambda sor : sor.nev == bekeres, kraterek))

if len(kereso) > 0:
    print(f"A(z) {bekeres} középpontja X={kereso[0].x} Y={kereso[0].y} sugara R={kereso[0].radius}. ")
else:
    print("Nincs ilyen nevű kráter.")

legnagyobb = max(kraterek, key=lambda sor:sor.radius)

legnagyobb_alt = list(filter(lambda sor:sor.radius==max([sor.radius for sor in kraterek]), kraterek))

print(f"""4. feladat
A legnagyobb kráter neve és sugara: {legnagyobb.nev} {legnagyobb.radius}""")

#print(f"4. feladat\nA legnagyobb kráter neve és sugara: {legnagyobb_alt[0].nev} {legnagyobb_alt[0].radius}")

def tavolsag(x1, y1, x2, y2 ):
  return ((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**0.5

"""6. Két kráter nem fedi át egymást, nincs közös részük, ha középpontjaik távolsága nagyobb,
mint a két kráter sugarának összege. Kérje be egy kráter nevét, és adja meg azoknak
a krátereknek a nevét, amelyekkel a bekért kráternek nincs közös része! A kiírásban
szereplő kráterek nevei között egy vessző és egy szóköz legyen az elválasztás! Ha nincs
ilyen kráter, akkor nem kell megjelenítenie semmit. """
print("6. feladat")

bekeres=input("Kérem egy kráter nevét: ")
nincs_kozos = []
krater_adatai = [sor for sor in kraterek if sor.nev == bekeres]

for sor in kraterek:
    tav = tavolsag(krater_adatai[0].x,krater_adatai[0].y, sor.x, sor.y)
    if tav > (krater_adatai[0].radius + sor.radius):
        nincs_kozos.append(sor.nev)

print(f"Nincs közös része: ",end="")

print(*nincs_kozos, sep=", ", end='.')


#magamtol sikerült jupiiiiiii

"""
7. Egy kráter tartalmaz egy másik krátert, ha a kisebb kráter teljes egészében a nagy kráterben
található. Ez körök esetében azt jelenti, hogy a két kör középpontjának távolsága kisebb,
mint a nagyobb kör sugarának és a kisebb kör sugarának különbsége. Vizsgálja meg
a krátereket, és írja ki azoknak a krátereknek a nevét, amelyek esetében a nagyobb kráter
tartalmazza a kisebb krátert! Minden ilyen tartalmazást csak egyszer jelenítsen meg úgy,
hogy megadja, hogy melyik kráter tartalmazza a másikat! 
"""


kor_a_korben = []

for index in range(1,len(kraterek)):
    kisebb=None
    nagyobb = None
    if kraterek[index].radius > kraterek[index-1].radius:
        nagyobb = kraterek[index].radius
        kisebb = kraterek[index-1].radius
    else:
        nagyobb = kraterek[index-1].radius
        kisebb = kraterek[index].radius


#folyt.köv még nincs kész 



"""
8. A kráterek adatai alapján számítsa ki, hogy mekkora területűek az egyes kráterek, és
készítsen egy terulet.txt szöveges állományt, amely tartalmazza a kráterek nevét és
területét! A kör területe 𝑇ൌ𝑟ଶ𝜋 ahol r a kör sugara, 𝜋 értéke két tizedesjegyre kerekítve
3.14. Az állomány minden egyes sorában egy kráter adatai szerepeljenek: először a kráter
területe két tizedesjegyre kerekítve, majd egy tabulátor karakter, majd a kráter neve! 
"""
"""
Minta a terulet.txt szöveges állomány kialakításához:
46.78 George Ogden Abell
4.01 Robert Henry Dicke
26.23 Abu Bakr ibn Tufajl
0.38 Stephen Hawking
... 
"""

with open("terulet.txt", "w") as f2:
    for sor in kraterek:
        print(f"{((sor.radius**2) * 3.14):.2f} {sor.nev}",file=f2)



