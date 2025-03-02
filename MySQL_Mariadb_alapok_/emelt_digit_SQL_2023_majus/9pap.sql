/*
9. Készítsen lekérdezést, amely megadja azoknak a szinkronszínészeknek a nevét, akik
valamely film szinkronizálásában együtt dolgoztak „Pap Kati” szinkronszínésszel!
A lekérdezés a hangjukat adó színészek nevét és a film magyar címét jelenítse meg!
A lekérdezés legyen a film magyar címe, azon belül a megjelenő szinkronszínészek neve
szerint ábécérendben, és ne tartalmazza „Pap Kati” nevét! (9pap)
*/

SELECT szinkron.hang, film.cim FROM film, szinkron
WHERE film.filmaz = szinkron.filmaz AND film.cim IN (SELECT film.cim FROM film,szinkron
WHERE film.filmaz = szinkron.filmaz AND szinkron.hang = "Pap Kati") AND szinkron.hang <> "Pap Kati"
ORDER by film.cim, szinkron.hang;

