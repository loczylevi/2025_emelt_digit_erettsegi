/*8. Készítsen lekérdezést, amely megadja, hogy kik azok a producerek, akiknek egyetlen
Oscar-díjra jelölt filmje esetén sem ismert a magyarországi bemutató dátuma! (8nemismert) */


SELECT keszito.nev FROM film,kapcsolat,keszito
WHERE film.id = kapcsolat.filmid AND kapcsolat.keszitoid = keszito.id AND film.bemutato IS NOT NULL
GROUP BY keszito.nev
HAVING COUNT(film.id) <> 1;


SELECT keszito.nev
    FROM keszito
    WHERE keszito.id NOT IN
      (
      SELECT kapcsolat.keszitoid
      FROM kapcsolat, film
      WHERE kapcsolat.filmid=film.id
      AND film.bemutato IS NOT NULL
      )
      AND keszito.producer;