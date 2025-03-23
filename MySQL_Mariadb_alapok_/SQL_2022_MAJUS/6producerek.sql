/*6. Vannak olyan producerek, akiknek több filmjét is jelölték díjra, e feladatban őket keressük.
Készítsen lekérdezést, amely megadja, hogy hány év telt el a legelső és a legutolsó jelölés
között! Jelenítse meg a producer nevét, a jelölések számát és az első és utolsó jelölés között
eltelt időt! (6producerek) */


SELECT keszito.nev, COUNT(film.nyert), max(film.ev)-MIN(film.ev) FROM film,kapcsolat,keszito
WHERE film.id = kapcsolat.filmid AND kapcsolat.keszitoid = keszito.id AND keszito.producer = 1
GROUP BY keszito.nev
HAVING COUNT(film.id) > 1;

SELECT keszito.nev, MAX(film.ev)-MIN(film.ev) AS eltelt, COUNT(film.id) AS db
    FROM film, kapcsolat, keszito
    WHERE film.id=kapcsolat.filmid AND kapcsolat.keszitoid=keszito.id
      AND keszito.producer
    GROUP BY keszito.nev
    HAVING COUNT(film.id)>1;
