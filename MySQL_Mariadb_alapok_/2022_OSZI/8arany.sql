/*8. Készítsen lekérdezést, amely megadja, hogy melyik megyében volt a legnagyobb
a felmérésben részt vevő tanulók aránya! A megye nevét és az arányt jelenítse meg!
(8arany) */

/*8. Készítsen lekérdezést, amely megadja, hogy melyik megyében volt a legnagyobb
a felmérésben részt vevő tanulók aránya! A megye nevét és az arányt jelenítse meg!
(8arany) */

SELECT megye.nev, aerob.letszam / megye.letszam as arany from megye, aerob
WHERE megye.kod = aerob.mkod
ORDER BY arany DESC
LIMIT 1;

SELECT megye.nev, SUM(aerob.letszam)/megye.letszam
FROM megye, aerob
WHERE mkod=megye.kod
GROUP BY megye.nev
ORDER BY 2 DESC
LIMIT 1; 
