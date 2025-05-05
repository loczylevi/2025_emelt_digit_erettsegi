-- 2. feladat
SELECT bajnok.ev, versenyszam.nev
FROM versenyszam, jatekos, bajnok
WHERE jatekos.id = bajnok.jatekos_id 
	AND versenyszam.id = bajnok.vsz_id 
	AND jatekos.nev = "Harczi Zsolt";

-- 3. feladat
SELECT Min(ev) AS Első_vegyes_páros
FROM versenyszam, bajnok
WHERE versenyszam.id = bajnok.vsz_id 
	AND versenyszam.nev = "vegyes páros";

-- 4. feladat
-- IF függvény: https://www.w3schools.com/mysql/func_mysql_if.asp
SELECT Count(*), IF(jatekos.neme = 0,"nő","férfi")
FROM jatekos
GROUP BY jatekos.neme;

-- 5. feladat
SELECT egyesulet.orszag
FROM egyesulet, bajnok
WHERE egyesulet.id = bajnok.egyesulet_id 
	AND bajnok.ev > 2000
GROUP BY egyesulet.orszag
HAVING egyesulet.orszag <> 'Magyarország';

-- 6. feladat
SELECT jatekos.nev
FROM jatekos, egyesulet, bajnok
WHERE egyesulet.id = bajnok.egyesulet_id 
	AND jatekos.id = bajnok.jatekos_id 
	AND egyesulet.nev = "MTK"
GROUP BY jatekos.id
ORDER BY jatekos.neme, jatekos.nev;

-- 7. feladat
SELECT jatekos.nev, bajnok.ev, versenyszam.nev
FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id 
	AND versenyszam.id = bajnok.vsz_id 
	AND bajnok.jatekos_id 
		IN (SELECT bajnok.jatekos_id
            FROM bajnok
            GROUP BY bajnok.jatekos_id
            HAVING COUNT(*) = 1);

-- 8. feladat
SELECT nev, max(bajnok.ev) - min(bajnok.ev)
FROM jatekos, bajnok
WHERE jatekos.id = bajnok.jatekos_id
GROUP BY jatekos.id
HAVING max(bajnok.ev) - min(bajnok.ev) >= 10
ORDER BY 2 DESC;

-- 9. feladat
SELECT DISTINCT jatekos.nev
FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id 
	AND bajnok.vsz_id = versenyszam.id 
	AND jatekos.nev <> 'Pergel Szandra' 
	AND versenyszam.nev = 'vegyes páros' 
	AND bajnok.ev IN (SELECT bajnok.ev
					 FROM jatekos, bajnok, versenyszam
					 WHERE jatekos.id = bajnok.jatekos_id 
						AND bajnok.vsz_id = versenyszam.id 
						AND versenyszam.nev = 'vegyes páros' 
						AND jatekos.nev = 'Pergel Szandra' );