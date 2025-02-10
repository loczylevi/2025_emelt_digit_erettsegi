/*6. Lekérdezés segítségével határozza meg, hogy melyik az az ingatlan, amelyet a legrégebben
hirdettek meg, de még nem adtak el, és amelynek a hirdetését sem módosították! Jelenítse
meg a közterület nevét és a házszámot, valamint a hirdetés feladásának dátumát! Ha több
ilyen ingatlan van, akkor elég az egyik
adatait megjelenítenie. (6eladatlan)*/

SELECT min(hirdetes.datum), ingatlan.kozterulet, ingatlan.hazszam FROM hirdetes
INNER JOIN ingatlan
ON hirdetes.ingatlanid = ingatlan.id
WHERE hirdetes.allapot <> "eladva" AND hirdetes.allapot <> "módosítva";


SELECT MIN(hirdetes.datum), ingatlan.kozterulet, ingatlan.hazszam FROM hirdetes, ingatlan
WHERE hirdetes.ingatlanid = ingatlan.id AND hirdetes.allapot <> "eladva"
GROUP BY hirdetes.ingatlanid
HAVING COUNT(hirdetes.ingatlanid) = 1
LIMIT 1;


SELECT kozterulet, hazszam, datum
FROM ingatlan, hirdetes
WHERE ingatlan.id=ingatlanid
GROUP BY ingatlan.id
HAVING Count(hirdetes.id)=1
ORDER BY datum
LIMIT 1;

