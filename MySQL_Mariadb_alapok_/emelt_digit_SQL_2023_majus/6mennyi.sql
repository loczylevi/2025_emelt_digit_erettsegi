/*6. Lekérdezés segítségével adja meg, hogy melyik filmben hány szereplő szinkronhangját
tartalmazza az adatbázis! Jelenítse meg a filmek eredeti és magyar címét, valamint
a szinkronszerepek számát! (6mennyi) 
 */

SELECT film.eredeti,film.cim, COUNT(szinkron.szerep) FROM film,szinkron
WHERE film.filmaz = szinkron.filmaz
GROUP BY film.filmaz;