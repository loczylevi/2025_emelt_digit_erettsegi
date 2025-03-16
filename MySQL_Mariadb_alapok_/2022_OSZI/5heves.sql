/*5. Lekérdezés segítségével adja meg, hogy hány megyében van kevesebb tanuló, mint
„Heves” megyében! (5heves)*/

SELECT count(megye.nev)
FROM megye
WHERE megye.letszam < (SELECT megye.letszam
 				 FROM megye
 				 WHERE megye.nev="Heves");