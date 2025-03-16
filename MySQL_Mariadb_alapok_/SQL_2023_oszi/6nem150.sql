/*6. Eredetileg úgy tervezték, hogy minden feladatsor 150 pontos lesz. Néhány esetben a kitűzés
után kellett módosítani a feladatsoron, így ez nem valósult meg. Adja meg lekérdezéssel
azokat a feladatsorokat, amelyek nem 150 pontosak! A feladatsor névadóját, a művészeti
ágat és a pontszámot jelenítse meg! (6nem150)  */


SELECT feladatsor.nevado, feladatsor.ag,sum(feladat.pontszam) FROM feladat, feladatsor
WHERE feladatsor.id = feladat.feladatsorid
GROUP BY feladatsor.nevado
HAVING sum(feladat.pontszam) <> 150;