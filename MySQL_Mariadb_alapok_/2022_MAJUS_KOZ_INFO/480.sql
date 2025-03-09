/*4. A 80-as vonal az egyik leghosszabb hazánkban. Készítsen lekérdezést, amely a kiinduló
állomástól mért távolság sorrendjében megjeleníti a működő állomások nevét, típusát és az
indulási állomástól mért távolságát! (480) */

/*
4. A 80-as vonal az egyik leghosszabb hazánkban. Készítsen lekérdezést, amely a kiinduló
állomástól mért távolság sorrendjében megjeleníti a működő állomások nevét, típusát és az
indulási állomástól mért távolságát! (480) 
*/

SELECT allomas.nev, allomas.tipus, hely.tav FROM allomas,tav
WHERE allomas.id = hely.allomasid
ORDER BY hely.tav ASC;
	


