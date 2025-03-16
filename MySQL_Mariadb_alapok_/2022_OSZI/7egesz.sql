/*7. Adja meg lekérdezés segítségével, hogy melyik megyében hány „egészséges” besorolást
kapott lány tanuló van! A lekérdezés a megye nevét és az egészséges tanulók számát adja
meg ez utóbbi szerint csökkenő sorrendben! (7egesz) */

SELECT megye.nev,SUM(aerob.letszam) as egeszseg FROM megye, aerob, allapot
WHERE megye.kod = aerob.mkod AND aerob.allkod = allapot.kod AND allapot.nev LIKE "%egészséges%" AND aerob.nem = 0
GROUP BY megye.nev
ORDER BY egeszseg DESC;


SELECT megye.nev, aerob.letszam
FROM aerob, megye, allapot
WHERE mkod=megye.kod AND allkod=allapot.kod AND nem=0 AND
 allapot.nev="egészséges"
ORDER BY 2 DESC; 