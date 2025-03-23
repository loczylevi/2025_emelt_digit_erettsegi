/*4. Készítsen lekérdezést, amely megadja azon filmek eredeti címét, amelyeket a második
világháború éveiben (1939 és 1945 között, a határokat is beleértve) jelöltek és ebben az
időszakban be is mutattak hazánkban! (4vh)*/

/*4. Készítsen lekérdezést, amely megadja azon filmek eredeti címét, amelyeket a második
világháború éveiben (1939 és 1945 között, a határokat is beleértve) jelöltek és ebben az
időszakban be is mutattak hazánkban! (4vh)*/

SELECT film.cim, film.ev FROM film 
WHERE 1939 <= film.ev AND 1945 >= film.ev AND bemutato BETWEEN "1939-1-1" AND "1945-12-31";


 SELECT film.cim
    FROM film
    WHERE ev BETWEEN 1939 And 1945
      AND bemutato BETWEEN "1939-01-01" AND "1945-12-31";