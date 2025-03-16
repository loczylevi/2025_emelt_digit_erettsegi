/*4. Készítsen lekérdezést, amely megadja, hogy összesen hány fiú tanuló kapott egészséges
besorolást „Zala” megyéből! (4zala) 
*/

SELECT sum(aerob.letszam) FROM megye, aerob, allapot
WHERE megye.kod = aerob.mkod AND aerob.allkod = allapot.kod
AND megye.nev = "Zala" AND aerob.nem = 1 AND
allapot.nev LIKE "%egészséges%";
