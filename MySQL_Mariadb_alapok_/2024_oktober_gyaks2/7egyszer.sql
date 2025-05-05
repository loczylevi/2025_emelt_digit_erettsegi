/*7. Lekérdezés segítségével listázza ki azokat a játékosokat, akik csak egyszer és egyetlen
bajnoki címet nyertek! A listában a nevük, a bajnoki cím éve és versenyszámuk neve
jelenjen meg! (7egyszer) 
*/

SELECT jatekos.nev, bajnok.ev, versenyszam.nev FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id AND bajnok.vsz_id = versenyszam.id
GROUP BY bajnok.jatekos_id
HAVING COUNT(*) = 1;
