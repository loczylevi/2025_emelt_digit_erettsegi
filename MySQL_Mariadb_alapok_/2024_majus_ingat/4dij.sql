/*4. Készítsen lekérdezést, amely megadja, hogy a közvetítő cég az itt szereplő ingatlanok
eladásából mennyi bevételre tett szert 2021-ben, ha az eladási ár 1,5 százalékát mint
közvetítői díjat megkapta! (4dij)*/


SELECT SUM(hirdetes.ar)* 0.015 AS osszegeg FROM hirdetes
WHERE YEAR(hirdetes.datum) = 2021 and hirdetes.allapot = "eladva";


SELECT SUM(hirdetes.ar)* 0.015 AS osszeg FROM hirdetes
WHERE YEAR(hirdetes.datum) = "2021" and hirdetes.allapot = "eladva";
