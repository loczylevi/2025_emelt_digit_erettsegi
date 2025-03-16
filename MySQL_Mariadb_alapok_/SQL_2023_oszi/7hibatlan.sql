/*7. Lekérdezés segítségével listázza ki azon csapatok nevét, amelyeknek volt maximális
pontszámot érő feladata! Minden csapat neve egyszer jelenjen meg! (7hibatlan) */

SELECT csapat.nev FROM csapat, feladat, megoldas, feladatsor
WHERE feladatsor.id = feladat.feladatsorid AND feladat.id = megoldas.feladatid AND megoldas.csapatid = csapat.id AND feladat.pontszam = megoldas.pontszam;



