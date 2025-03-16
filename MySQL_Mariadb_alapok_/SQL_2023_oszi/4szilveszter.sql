/*5. Készítsen lekérdezést, amely meghatározza a végeredményt! A csapatok neve és az általuk
elért összpontszám jelenjen meg, utóbbi szerint csökkenő sorrendben! (5eredmeny) */

SELECT feladatsor.nevado FROM feladatsor WHERE feladatsor.kituzes < "2018.12.31" AND feladatsor.hatarido > "2018.12.31";

