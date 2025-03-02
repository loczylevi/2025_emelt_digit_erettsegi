/*
8. Lekérdezés segítségével listázza ki azoknak a versenyzőknek a nevét, akiknek az első és
utolsó bajnoki címe között legalább 10 év telt el! A listában a nevek és az eltelt évek száma
jelenjen meg, az utóbbiak szerint csökkenő sorrendben! (8sokaig) 
*/

SELECT jatekos.nev, (Max(bajnok.ev) - Min(bajnok.ev)) as idotav FROM jatekos,bajnok
WHERE jatekos.id = bajnok.jatekos_id 
GROUP by bajnok.jatekos_id
HAVING (Max(bajnok.ev) - Min(bajnok.ev)) > 10
ORDER by (Max(bajnok.ev) - Min(bajnok.ev)) > 10 DESC;
