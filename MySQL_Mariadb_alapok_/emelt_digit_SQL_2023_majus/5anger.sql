/*5. Lekérdezés segítségével adja meg, hogy mely filmekben, milyen szerepekhez és mely
színészeknek kölcsönözte a hangját „Anger Zsolt”! A film magyar és eredeti címét,
valamint a szinkronizált színész és a játszott karakter nevét jelenítse meg! (5anger) */

SELECT film.eredeti, film.cim, szinkron.szerep, szinkron.szinesz FROM film,szinkron
WHERE film.filmaz = szinkron.filmaz AND szinkron.hang = "Anger Zsolt";