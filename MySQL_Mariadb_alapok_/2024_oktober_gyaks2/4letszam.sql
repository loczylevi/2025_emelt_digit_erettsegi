/*4. Lekérdezés segítségével adja meg, hogy hány férfi és hány női játékos van az adatbázisban!
A létszám értékei mellett a nemek felirata is jelenjen meg! Segítségképpen az elágazás
függvény használata SQL-ben: IF(feltétel, érték1, érték2) eredménye, ha a
feltétel igaz, akkor érték1, különben érték2. (4letszam)  */

SELECT COUNT(*), IF(jatekos.neme = 1, "Férfi", "Nő")  FROM jatekos
GROUP BY jatekos.neme;

