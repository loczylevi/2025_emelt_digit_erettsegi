/*8. Bár a versenyzők lelkesek voltak és törekedtek minden feladatot megoldani, ennek ellenére
előfordult, hogy nem minden feladatra adtak be megoldást. Készítsen lekérdezést, amely
megadja, hogy a „#win” csapat mely feladatsorokból hány feladatot nem adott be! Jelenítse
meg a feladatsor névadóját és a be nem adott feladatok számát! (8#win) */

SELECT csapat.nev, feladatsor.nevado, COUNT(feladat.pontszam) FROM csapat,feladatsor,megoldas,feladat
WHERE csapat.nev = "#win" AND feladatsor.id = feladat.feladatsorid AND feladat.id = megoldas.feladatid AND megoldas.csapatid = csapat.id
GROUP BY feladatsor.id
HAVING COUNT(feladat.id) = 0;



