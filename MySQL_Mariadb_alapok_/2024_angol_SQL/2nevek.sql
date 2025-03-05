/*2. Lekérdezés segítségével írassa ki a ragadványnévvel rendelkező királyok nevét és
ragadványnevét a születési évük sorrendjében! (2nevek) */



SELECT ragnev,szul FROM uralkodo
WHERE ragnev IS NOT NULL
ORDER BY szul ASC;
