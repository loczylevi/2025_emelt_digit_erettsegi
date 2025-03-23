/*2. Készítsen lekérdezést, amely az elismerés évének sorrendjében jeleníti meg az Oscar-díjas
filmeket! Az elnyerés éve és a film eredeti címe jelenjen meg! (2nyertes) */

SELECT film.ev, film.cim FROM film
WHERE film.nyert = 1
ORDER BY film.ev;