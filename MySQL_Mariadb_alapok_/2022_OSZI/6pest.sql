/*6. Lekérdezés segítségével adja meg, hogy „Pest” megyében a tanulók hányadrésze vett részt
a felmérésben! (6pest) */

SELECT sum(aerob.letszam) / (SELECT sum(aerob.letszam) FROM megye,aerob
WHERE megye.kod = aerob.mkod AND megye.nev = "Pest") FROM megye,aerob
WHERE megye.kod = aerob.mkod;

SELECT (SELECT sum(aerob.letszam) FROM megye,aerob
WHERE megye.kod = aerob.mkod AND megye.nev = "Pest") / sum(aerob.letszam)  FROM megye,aerob
WHERE megye.kod = aerob.mkod;

SELECT sum(aerob.letszam)/megye.letszam
FROM aerob, megye
WHERE mkod=kod AND nev="Pest";