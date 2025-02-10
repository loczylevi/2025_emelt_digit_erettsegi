SELECT hirdetes.ar, ingatlan.hazszam FROM ingatlan
INNER JOIN hirdetes
ON hirdetes.ingatlanid = ingatlan.id
WHERE ingatlan.kozterulet LIKE "%Agyagos utca%" 
