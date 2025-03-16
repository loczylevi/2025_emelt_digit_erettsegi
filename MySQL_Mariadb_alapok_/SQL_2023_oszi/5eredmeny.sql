/*5. Készítsen lekérdezést, amely meghatározza a végeredményt! A csapatok neve és az általuk
elért összpontszám jelenjen meg, utóbbi szerint csökkenő sorrendben! (5eredmeny) */

SELECT csapat.nev, sum(megoldas.pontszam) as ponty FROM csapat, megoldas
WHERE megoldas.csapatid = csapat.id 
GROUP BY csapat.id
ORDER BY ponty DESC;

