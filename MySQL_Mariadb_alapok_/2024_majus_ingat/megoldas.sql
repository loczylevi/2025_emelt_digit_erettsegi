-- 2. feladat
SELECT DISTINCT ingatlan.kozterulet
FROM ingatlan
WHERE ingatlan.lakas
ORDER BY ingatlan.kozterulet;

-- 3. feladat
SELECT ingatlan.hazszam, hirdetes.ar
FROM ingatlan, hirdetes
WHERE ingatlan.id = hirdetes.ingatlanid
	AND hirdetes.allapot = 'meghirdetve'
	AND ingatlan.kozterulet = 'Agyagos utca';

-- 4. feladat
SELECT SUM(hirdetes.ar * 0.015)
FROM hirdetes
WHERE hirdetes.allapot = 'eladva'
	AND YEAR(hirdetes.datum) = 2021;

-- 5. feladat
SELECT MAX(hirdetes.ar) / MIN(hirdetes.ar)
FROM hirdetes
WHERE hirdetes.allapot = 'meghirdetve';

-- 6. feladat
SELECT ingatlan.kozterulet, ingatlan.hazszam, hirdetes.datum
FROM ingatlan, hirdetes
WHERE ingatlan.id = hirdetes.ingatlanid
GROUP BY hirdetes.ingatlanid
HAVING COUNT(*) = 1
ORDER BY hirdetes.datum
LIMIT 1;

-- 7. feladat
SELECT ingatlan.kozterulet, ingatlan.hazszam, hirdet.ar
FROM ingatlan, hirdetes AS hirdet, hirdetes AS elad
WHERE ingatlan.id = hirdet.ingatlanid
	AND hirdet.ingatlanid = elad.ingatlanid
	AND hirdet.allapot = 'meghirdetve'
	AND elad.allapot = 'eladva'
	AND hirdet.ar = elad.ar;

-- 8. feladat
SELECT kozterulet, hazszam
FROM ingatlan
WHERE id NOT IN (SELECT helyiseg.ingatlanid 
				FROM helyiseg
				WHERE helyiseg.funkcio = 'konyha')
	AND id NOT IN (SELECT helyiseg.ingatlanid
					FROM helyiseg
					WHERE helyiseg.funkcio = 'WC');


-- 9. feladat
SELECT ingatlan.kozterulet, ingatlan.hazszam, 
	SUM(helyiseg.hossz * helyiseg.szel * IF(funkcio = "terasz", 0.5, 1)) AS terulet
FROM ingatlan, helyiseg
WHERE ingatlan.id = helyiseg.ingatlanid
GROUP BY helyiseg.ingatlanid
HAVING terulet > 180;
