/*
3. Készítsen lekérdezést, amely az adatbázisban tárolt adatok alapján megjeleníti a jelenleg
Magyarországon kívül található állomások nevét és ország jelét, az állomásnév szerint
ábécérendben! (3kulfold) 
*/

SELECT allomas.nev, allomas.orszag from allomas
WHERE allomas.orszag <> ""
ORDER by allomas.nev ASC;

SELECT allomas.nev, allomas.orszag from allomas
WHERE NOT allomas.orszag = ""
ORDER by allomas.nev ASC;



