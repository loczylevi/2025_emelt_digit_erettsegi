/*3. Készítsen lekérdezést, amely meghatározza, hogy melyik évben adták ki a „vegyes páros”
bajnoki címet először! (3vegyes)*/

SELECT MIN(bajnok.ev) FROM bajnok, versenyszam
WHERE bajnok.vsz_id = versenyszam.id AND versenyszam.nev = "vegyes páros";

SELECT bajnok.ev FROM bajnok, versenyszam
WHERE bajnok.vsz_id = versenyszam.id AND versenyszam.nev = "vegyes páros";

SELECT bajnok.ev FROM bajnok, versenyszam
WHERE bajnok.vsz_id = versenyszam.id AND versenyszam.nev = "vegyes páros"
ORDER BY bajnok.ev ASC
LIMIT 1;

