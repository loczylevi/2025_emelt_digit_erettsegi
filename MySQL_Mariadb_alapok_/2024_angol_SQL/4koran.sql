/*4. Lekérdezés segítségével sorolja fel azoknak a királyoknak a nevét, akik már a koronázásuk
éve előtt elfoglalták a hivatalukat! (4koran) */

SELECT uralkodo.nev FROM uralkodo,hivatal
WHERE uralkodo.azon = hivatal.uralkodo_az AND hivatal.mettol < hivatal.koronazas