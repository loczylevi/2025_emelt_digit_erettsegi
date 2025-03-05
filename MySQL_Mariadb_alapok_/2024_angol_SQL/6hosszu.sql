/*6. Készítsen lekérdezést, amely meghatározza, hogy ki uralkodott a leghosszabb ideig
egyfolytában és hány évet? Az uralkodás hosszának számítása például: I. István 1000-től
1038-ig uralkodott, tehát 39 évig volt magyar király. (6hosszu) */

SELECT meddig-mettol as uralkodas, uralkodo.nev FROM hivatal,uralkodo
WHERE hivatal.uralkodo_az = uralkodo.azon
ORDER by uralkodas DESC
LIMIT 1;

