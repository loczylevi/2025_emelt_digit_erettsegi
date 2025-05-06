/*6. Lekérdezés segítségével határozza meg, hogy melyik az az ingatlan, amelyet a legrégebben
hirdettek meg, de még nem adtak el, és amelynek a hirdetését sem módosították! Jelenítse
meg a közterület nevét és a házszámot, valamint a hirdetés feladásának dátumát! Ha több
ilyen ingatlan van, akkor elég az egyik adatait megjelenítenie. (6eladatlan) */


SELECT ingatlan.kozterulet, ingatlan.hazszam, hirdetes.datum FROM ingatlan, hirdetes
WHERE hirdetes.ingatlanid = ingatlan.id AND hirdetes.allapot = "meghirdetve"
GROUP BY hirdetes.ingatlanid
HAVING COUNT(*) = 1
ORDER BY hirdetes.datum ASC
LIMIT 1;