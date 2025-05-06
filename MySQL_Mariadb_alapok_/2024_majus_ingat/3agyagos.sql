/*3. Lekérdezés segítségével adja meg, hogy az „Agyagos utca” ingatlanjait milyen áron
hirdették meg! Jelenítse meg a házszámot és a meghirdetéskor megadott árat! (3agyagos) 
*/

SELECT ingatlan.kozterulet, hirdetes.ar FROM ingatlan, hirdetes
WHERE hirdetes.ingatlanid = ingatlan.id AND ingatlan.kozterulet = "Agyagos utca" AND  hirdetes.allapot = "meghirdetve";
