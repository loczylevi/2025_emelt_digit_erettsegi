/*2. Készítsen lekérdezést, amely megadja, hogy az adatbázisban milyen közterületeken
kínálnak lakást! Minden közterület neve csak egyszer, ábécérendben jelenjen meg!
(2kozterulet) */

SELECT DISTINCT ingatlan.kozterulet FROM ingatlan
WHERE ingatlan.lakas = 1
ORDER BY ingatlan.kozterulet ASC;

SELECT DISTINCT ingatlan.kozterulet FROM ingatlan
WHERE ingatlan.lakas 
ORDER BY ingatlan.kozterulet ASC;