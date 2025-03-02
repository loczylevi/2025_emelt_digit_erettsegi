/*4. Készítsen lekérdezést, amely megadja azokat a magyar szövegírókat, akik „Christopher
Nolan” rendező valamely filmjének magyar szövegét írták egy a „Mafilm Audio Kft.”
stúdióban készült szinkronhoz! A lekérdezés az írót és a film magyar nyelvű címét jelenítse
meg, az írók neve szerint ábécérendben! (4szoveg) */

SELECT film.magyarszoveg, film.cim FROM film 
WHERE film.rendezo = "Christopher Nolan"
AND film.studio = "Mafilm Audio Kft."
ORDER BY film.magyarszoveg ASC;