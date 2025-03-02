/*8. Lekérdezés segítségével adja meg azokat a személyeket, akik filmrendezőként és
színészként is szerepelnek az adatbázisban (nem feltétlenül ugyanabban a filmben)!
A lekérdezés egyszer tartalmazza az ilyen személyek nevét! A lekérdezésben megjelenő
mező neve legyen „Színész-rendező”! (8rendszin) 
*/

/*
8. Lekérdezés segítségével adja meg azokat a személyeket, akik filmrendezőként és
színészként is szerepelnek az adatbázisban (nem feltétlenül ugyanabban a filmben)!
A lekérdezés egyszer tartalmazza az ilyen személyek nevét! A lekérdezésben megjelenő
mező neve legyen „Színész-rendező”! (8rendszin)
*/
-- szerep --> rab like

SELECT DISTINCT film.rendezo AS "Színész-rendező" FROM film,szinkron
WHERE film.filmaz = szinkron.filmaz AND film.rendezo = szinkron.szinesz;

SELECT DISTINCT film.rendezo AS "Színész-rendező" FROM film
WHERE film.rendezo IN (SELECT szinkron.szinesz FROM szinkron);