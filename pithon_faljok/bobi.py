class Rendeles:
    def __init__(self,sor):
        nap,varos,db= sor.strip().split()
        self.nap = int(nap)
        self.varos = str(varos)
        self.db = int(db)
        
with open("rendel.txt") as f:
    lista = [Rendeles(sor) for sor in f]
    
print(f"""2. feladat:
A rendelések száma: {len(lista)} """)

print("3. feladat:")
bekeres = int(input("Kérem, adjon meg egy napot: "))

hany_rendeles = len([sor.db for sor in lista if bekeres == sor.nap])
hany_rendeles2 = len(list(filter(lambda sor : bekeres == sor.nap, lista)))

print(f"A rendelések száma az adott napon: {hany_rendeles} ")

print(f"""4. feladat:
{len([sor for sor in lista if sor.varos == "NR"])} nap nem volt a reklámban nem érintett városból rendelés """)


print(f"""5. feladat:
A legnagyobb darabszám: {max(lista, key=lambda sor :sor.db).db}, a rendelés napja: {max(lista, key=lambda sor :sor.db).nap}""")


"""
6. Készítsen függvényt osszes néven, amely megadja, hogy mennyi volt egy adott városból
egy adott napon a rendelt termékek száma! A függvény bemenete a három város egyikére
utaló kétbetűs szöveg és a nap sorszáma legyen. Amennyiben szükséges, akkor további
paramétert is felvehet a rendelések adatainak elérése érdekében. A függvény visszaadott
értéke a rendelt darabszámok összege legyen! A függvényt például a következő módon
lehessen meghívni: osszes("PL", 7). A függvényt a későbbiekben felhasználhatja
a további feladatok megoldásakor. """


    
    
    