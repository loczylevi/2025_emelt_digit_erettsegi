/*11. Készítsen lekérdezést, amely megadja, hogy mely feladatoksorokat tűzték ki az előző
beadási határidejét követő napon! A feladatsor névadóját és a kitűzés idejét jelenítse meg!
A feladat megoldása során kihasználhatja, hogy egyszerre csak egy feladatsor volt aktív.
(11rogton) */

SELECT F1.nevado, F1.kituzes FROM feladatsor F1, feladatsor F2
WHERE DATEDIFF(F1.kituzes, F2.hatarido) = 1;

SELECT kovetkezo.nevado, kovetkezo.kituzes
FROM feladatsor AS kovetkezo, feladatsor AS elozo
WHERE DATEDIFF(kovetkezo.kituzes, elozo.hatarido)=1; 