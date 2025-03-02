/*2. Lekérdezés segítségével írassa ki, hogy „Harczi Zsolt” mely években és milyen
versenyszámban szerzett bajnoki címet! (2harczi)*/

SELECT bajnok.ev, versenyszam.nev FROM bajnok, jatekos, versenyszam
WHERE jatekos.id = bajnok.jatekos_id AND jatekos.nev = "Harczi Zsolt"
AND bajnok.vsz_id = versenyszam.id;