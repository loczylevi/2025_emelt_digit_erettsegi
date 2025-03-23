/*3. Készítsen lekérdezést, amely megadja, hogy mely években jelöltek legalább 10 filmet a
díjra! Csak a jelölés évét jelenítse meg! (3min10)  */

SELECT film.ev FROM film
GROUP BY film.ev
HAVING COUNT(film.nyert) >= 10;

