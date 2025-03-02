/*3. Lekérdezés segítségével adja meg, azokat a filmrendezőket és szinkronrendezőket, akik
valamely 2000 után bemutatott filmet, illetve szinkronját rendezték! A lekérdezés minden
névpárt egyszer jelenítsen meg! (3szinkrend) */

SELECT DISTINCT film.rendezo,film.szinkronrendez FROM film
WHERE film.ev > 2000;  

