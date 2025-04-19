"""
. Egy sorban 9 adat szerepel, a jármű
rendszáma (6 karakteren), a szakasz kezdeti- és végpontján rögzített időpont óra, perc, másodperc,
ezredmásodperc formában. (A fájl olyan járművek adatait nem tartalmazza, amelyeknek a szakasz
kezdeti- vagy végpontján nem volt mérési értéke.) 
"""

#OJV879 8 11 21 310 8 19 2 849

class Szakasz_velocitas_ell:
    def __init__(self,sor):
        rendszam,kezd_ora,kezd_perc,kezd_sec,kezd_ezred,veg_ora,veg_perc,veg_sec,veg_ezred = sor.strip().split()
        self.rendszam = rendszam
        self.kezd_ora = int(kezd_ora)
        self.kezd_perc = int(kezd_perc)
        self.kezd_sec = int(kezd_sec)
        self.kezd_ezred = int(kezd_ezred)
        self.veg_ora = int(veg_ora)
        self.veg_perc = int(veg_perc)
        self.veg_sec = int(veg_sec)
        self.veg_ezred = int(veg_ezred)

#OJV879 8 11 21 310 8 19 2 849

with open("meresek.txt") as f:
    lista = [Szakasz_velocitas_ell(sor) for sor in f]
    
print(f"""2. feladat
A mérés során {len(lista)} jármű adatait rögzítették. 
""")

egy_sor = len([sor for sor in lista if sor.veg_ora < 9])

print(f"""3. feladat
9 óra előtt {len(list(filter(lambda sor : sor.veg_ora < 9, lista)))} jármű haladt el a végponti mérőnél. 
""")

print(f"""4. feladat""")
bekeres = input("Adjon meg egy óra és perc értéket! ")

szeletelo = bekeres.split()



print(f"""\ta. A kezdeti méréspontnál elhaladt járművek száma: {len(list(filter(lambda sor : sor.kezd_perc == int(szeletelo[1]), lista)))}
\tb. A forgalomsűrűség:  """)


#len(list(filter(lambda sor : 0 <= sor.kezd_sec <= 59 and 0 <= sor.kezd_ezred <= 999), lista))

xd = len([sor for sor in lista if 0 <= sor.kezd_sec <= 59 and 0 <= sor.kezd_ezred <= 999 and sor.kezd_ora == int(szeletelo[0]) and sor.kezd_perc == int(szeletelo[1])]) 
print (xd) 

"""5. Mekkora volt a legnagyobb átlagsebességgel haladó járműnek a
sebessége, és hány
járművet hagyott le a mért szakasz végére? Amennyiben több legnagyobb átlagsebesség
érték van, akkor elég az egyiket kiírnia. Az autó rendszámát, 
az átlagsebességet egész
számként és a lehagyott járművek számát jelenítse meg! """

def velocitas(k_o,k_p,k_m,k_e,v_o,v_p,v_m,v_e):
    k_ossz = k_o + (k_p/60) + (k_m + k_e/1000)/3600 
    v_ossz = v_o + (v_p/60) + (v_m + v_e/1000)/3600 
    ido_intervallum = v_ossz - k_ossz
    return 10 / ido_intervallum

sebessegek = max([[velocitas(sor.kezd_ora, sor.kezd_perc, sor.kezd_sec, sor.kezd_ezred, sor.veg_ora, sor.veg_perc, sor.veg_sec, sor.veg_ezred),sor ] for sor in lista] )

#atlag = sum(sebessegek) / len(sebessegek)
#print(sebessegek[0])
import math
jegnegyobb_xd = f"{math.floor(sebessegek[0])}"
print(f"""5. feladat
A legnagyobb sebességgel haladó jármű
 rendszáma: {sebessegek[1].rendszam}
 átlagsebessége: {math.floor(sebessegek[0])} km/h
 által lehagyott járművek száma: {len([sor for sor in lista if int(velocitas(sor.kezd_ora, sor.kezd_perc, sor.kezd_sec, sor.kezd_ezred, sor.veg_ora, sor.veg_perc, sor.veg_sec, sor.veg_ezred)) <= int(jegnegyobb_xd)])}
 """)

import math
xd = round(7.9)
xd2 = math.floor(7.9)



