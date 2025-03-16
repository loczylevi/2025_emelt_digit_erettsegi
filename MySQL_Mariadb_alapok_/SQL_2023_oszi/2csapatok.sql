/*2. Lekérdezés segítségével írassa ki azon csapatok nevét, amelyek neve a # karakterrel
kezdődik! (2csapatok) */

SELECT csapat.nev FROM csapat WHERE csapat.nev LIKE "#%";
