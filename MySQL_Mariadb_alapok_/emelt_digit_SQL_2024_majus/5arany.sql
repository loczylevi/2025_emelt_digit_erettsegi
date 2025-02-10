select MAX(hirdetes.ar) / MIN(hirdetes.ar) AS kulombseg FROM hirdetes
WHERE hirdetes.allapot NOT IN ("módosítva","eladva");
