/*5. Lekérdezés segítségével adja meg, hogy a legdrágábban meghirdetett ingatlan ára
hányszorosa volt a legolcsóbban meghirdetett ingatlan árának! Az árváltozásokat és
az eladásokat ne vegye figyelembe! Adja meg az arányt kerekítés nélkül! (5arany)*/


SELECT MAX(hirdetes.ar) / MIN(hirdetes.ar) FROM hirdetes
WHERE hirdetes.allapot = "meghirdetve" AND hirdetes.allapot <> "eladva" AND hirdetes.allapot <> "módosítva";