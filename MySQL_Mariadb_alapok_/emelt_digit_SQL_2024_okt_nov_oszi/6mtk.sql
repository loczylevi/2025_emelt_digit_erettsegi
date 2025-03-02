/*
6. Készítsen lekérdezést, amely felsorolja az „MTK” egyesület bajnok játékosainak nevét!
A listában először a nők, majd a férfiak jelenjenek meg, azon belül a nevek ábécérendben
ismétlődés nélkül! (6mtk) 
*/

SELECT DISTINCT jatekos.nev FROM jatekos,egyesulet,bajnok
WHERE bajnok.jatekos_id = jatekos.id AND bajnok.egyesulet_id = egyesulet.id AND egyesulet.nev = "MTK"
ORDER BY jatekos.neme ASC,jatekos.nev ASC;
