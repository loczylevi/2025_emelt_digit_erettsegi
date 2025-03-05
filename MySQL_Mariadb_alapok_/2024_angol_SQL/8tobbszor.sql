/*8. A történelmi események során előfordult, hogy az uralkodó a királyi hivatalt többször
foglalta el. Készítsen lekérdezést, amely meghatározza azoknak a királyoknak a nevét és
uralkodásuk összes idejét, akik többször foglalták el a hivatalt! (8tobbszor) 
*/

/*8. A történelmi események során előfordult, hogy az uralkodó a királyi hivatalt többször
foglalta el. Készítsen lekérdezést, amely meghatározza azoknak a királyoknak a nevét és
uralkodásuk összes idejét, akik többször foglalták el a hivatalt! (8tobbszor) 
*/
-- én megoldásom
SELECT uralkodo.nev, SUM(meddig-mettol) as uralkodas FROM uralkodo,hivatal
WHERE uralkodo.azon = hivatal.uralkodo_az 
GROUP BY hivatal.uralkodo_az
HAVING COUNT(hivatal.uralkodo_az) > 1;


-- megoldo kulcs alappján
SELECT nev, Sum(meddig-mettol+1)
FROM uralkodo, hivatal
WHERE uralkodo.azon = hivatal.uralkodo_az
GROUP BY nev
HAVING Count(hivatal.azon)>1; 
