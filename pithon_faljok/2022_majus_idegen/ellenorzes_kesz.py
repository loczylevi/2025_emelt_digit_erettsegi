"""
Egy sorban 9 adat szerepel, a jármű
rendszáma (6 karakteren), a szakasz kezdeti- és végpontján rögzített időpont óra, perc, másodperc,
ezredmásodperc formában. (A fájl olyan járművek adatait nem tartalmazza, amelyeknek a szakasz
kezdeti- vagy végpontján nem volt mérési értéke.) 
"""

#OJV879 8 11 21 310 8 19 2 849
try:
    
    class Szakasz_velocitas_ell:
        def __init__(self,sor):
            rendszam,kezd_ora,kezd_perc,kezd_sec,kezd_ezred,veg_ora,veg_perc,veg_sec,veg_ezred = sor.strip().split()
            self.rendszam = str(rendszam)
            self.kezd_ora = int(kezd_ora)
            self.kezd_perc = int(kezd_perc)
            self.kezd_sec = int(kezd_sec)            # ༼ つ ◕_◕ ༽つ
            self.kezd_ezred = int(kezd_ezred)
            self.veg_ora = int(veg_ora)
            self.veg_perc = int(veg_perc)
            self.veg_sec = int(veg_sec)
            self.veg_ezred = int(veg_ezred)
            self.start = self.kezd_ora + (self.kezd_perc/60) + (self.kezd_sec/3600) + ((self.kezd_ezred/1000)/3600)
            self.end = self.veg_ora + (self.veg_perc/60) + (self.veg_sec/3600) + ((self.veg_ezred/1000)/3600)

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

    #OJV879 8 11 21 310 8 19 2 849

    def orara_atvalto(ora,perc,masodperc,ezred):
        return ora + (perc/60) + (masodperc/3600) + ((ezred/1000)/3600)

    # 8 óra 20 perc 0 masod 0 ezredtöl 08:20:59,999 között

    meres_eleje = int(szeletelo[0]) + int(szeletelo[1])/60

    meres_vege = int(szeletelo[0]) + int(szeletelo[1])/60 + (59/3600) + (999/1000)/3600

    #ossz = int(szeletelo[0]) + (int(szeletelo[1])/60) 
    cuccmokos = []
    for sor in lista:
        if sor.start < meres_vege and sor.end > meres_eleje:
            cuccmokos.append(sor)


    b = len(cuccmokos) / 10
    #print(f"\n{b}")
    print(f"""\ta. A kezdeti méréspontnál elhaladt járművek száma: {len(list(filter(lambda sor : sor.kezd_perc == int(szeletelo[1]), lista)))}
    \tb. A forgalomsűrűség: {b} """)


    #len(list(filter(lambda sor : 0 <= sor.kezd_sec <= 59 and 0 <= sor.kezd_ezred <= 999), lista))

    xd = len([sor for sor in lista if 0 <= sor.kezd_sec <= 59 and 0 <= sor.kezd_ezred <= 999 and sor.kezd_ora == int(szeletelo[0]) and sor.kezd_perc == int(szeletelo[1])]) 


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
    import math
    sebessegek = max([[velocitas(sor.kezd_ora, sor.kezd_perc, sor.kezd_sec, sor.kezd_ezred, sor.veg_ora, sor.veg_perc, sor.veg_sec, sor.veg_ezred),sor ] for sor in lista] )
    jegnegyobb_xd = f"{math.floor(sebessegek[0])}"

    lehagyott = [[velocitas(sor.kezd_ora, sor.kezd_perc, sor.kezd_sec, sor.kezd_ezred, sor.veg_ora, sor.veg_perc, sor.veg_sec, sor.veg_ezred),sor ] for sor in lista] 

    db = 0
    for sor in lista:
        if sebessegek[1].start > sor.start and sebessegek[1].end < sor.end:
            db += 1

    #atlag = sum(sebessegek) / len(sebessegek)
    #print(sebessegek[0])
    import math

    print(f"""\n5. feladat
    A legnagyobb sebességgel haladó jármű
    rendszáma: {sebessegek[1].rendszam}
    átlagsebessége: {math.floor(sebessegek[0])} km/h
    által lehagyott járművek száma: {db}
    """)

    import math
    xd = round(7.9)
    xd2 = math.floor(7.9)

    """
    6. Határozza meg, hogy a járművek hány százalékának az átlagsebessége haladta meg az
    útszakaszon megengedett legnagyobb sebességet (90 km/h)! Az értéket tizedes tört alakban
    jelenítse meg a minta szerint! 
    """

    sebessegek2 = [[velocitas(sor.kezd_ora, sor.kezd_perc, sor.kezd_sec, sor.kezd_ezred, sor.veg_ora, sor.veg_perc, sor.veg_sec, sor.veg_ezred),sor ] for sor in lista] 


    nagyobb_mint_90_ven = []

    for sor in sebessegek2:
        if sor[0] > 90:
            nagyobb_mint_90_ven.append(sor[0])

    #print(nagyobb_mint_90_ven)
            
    xd = (len(nagyobb_mint_90_ven) / len(sebessegek2))

    print(f"""6. feladat
    A járművek {xd*100:.2f}%-a volt gyorshajtó. 
    """)

    print(f"""6. feladat
    A járművek {round(xd*100,2)}%-a volt gyorshajtó. 
    """)

    """
    104 km/h felett 121 km/h-ig 30 000 Ft
    121 km/h felett 136 km/h-ig 45 000 Ft
    136 km/h felett 151 km/h-ig 60 000 Ft
    151 km/h felett 200 000 Ft"""

    def buntetes(sebesseg):
        if 104 < sebesseg <= 121:
            return 30000
        if 121 < sebesseg <= 136:
            return 45000
        if 136 < sebesseg <= 151:
            return 60000
        if 151 < sebesseg:
            return 200000
        if 104 > sebesseg:
            return 0

    sebessegek2 = [[velocitas(sor.kezd_ora, sor.kezd_perc, sor.kezd_sec, sor.kezd_ezred, sor.veg_ora, sor.veg_perc, sor.veg_sec, sor.veg_ezred), sor.rendszam  ]for sor in lista]



    with open("buntetes.txt", "w") as f2:
        for sor in sebessegek2:
            if buntetes(sor[0]) == 0:
                pass
            else:
                print(f"{sor[1]}\t{sor[0]:.0f} km/h\t{buntetes(sor[0])} Ft", file=f2)

    print(f"A fájl elkészült. ")

except:
    print("valami nem jó gec")
finally:
    print("UwU")
