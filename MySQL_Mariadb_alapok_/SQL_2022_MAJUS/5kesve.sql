/*5. Készítsen lekérdezést, amely megadja, hogy mely nyertes filmek esetén volt a
magyarországi bemutató legalább 10 évvel később, mint a díjazás! Csak a film eredeti címét
jelenítse meg! (5kesve) */

SELECT film.cim FROM film 
where film.nyert = 1 AND YEAR(film.bemutato)-film.ev >= 10;




