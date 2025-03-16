/*3. Készítsen lekérdezést, amely megadja, hogy „Somogy” megyében hány tanuló vett részt
a felmérésben! (3somogy) */

SELECT megye.letszam FROM megye, aerob
WHERE megye.nev = "Somogy" AND megye.kod = aerob.mkod;