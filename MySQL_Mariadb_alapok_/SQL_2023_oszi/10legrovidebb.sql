/*10. Lekérdezés segítségével adja meg, melyik feladatsor megoldására volt a legkevesebb idő!
A feladatsor névadóját jelenítse meg! Ha több ilyen feladatsor van, elegendő az egyiket
megadnia. (10legrovidebb) */

-- én megoldásom
SELECT feladatsor.nevado, feladatsor.hatarido-feladatsor.kituzes as datum FROM feladatsor
ORDER BY datum DESC
LIMIT 1;

-- hivatalos
SELECT nevado, DATEDIFF(hatarido, kituzes)
FROM feladatsor
ORDER BY DATEDIFF(hatarido, kituzes) DESC
LIMIT 1; 