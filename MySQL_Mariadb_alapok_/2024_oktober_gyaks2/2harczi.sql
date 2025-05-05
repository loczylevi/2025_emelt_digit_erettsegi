/*3. Készítsen lekérdezést, amely meghatározza, hogy melyik évben adták ki a „vegyes páros”
bajnoki címet először! (3vegyes) */

SELECT bajnok.ev, versenyszam.nev  FROM jatekos, bajnok, versenyszam
WHERE jatekos.nev = "Harczi Zsolt" AND jatekos.id = bajnok.jatekos_id AND bajnok.vsz_id = versenyszam.id;