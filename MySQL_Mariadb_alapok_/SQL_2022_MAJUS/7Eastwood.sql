/*7. Nem ritka, hogy egy-egy filmnek több, akár három-négy producere is van. Készítsen
lekérdezést, amely megadja, hogy a jelölést kapott, azaz az adatbázisban tárolt filmekben
kik voltak „Clint Eastwood” producertársai! Az érintett személyek nevét jelenítse meg, és
biztosítsa, hogy mindenki csak egyszer szerepeljen! (7Eastwood) */

SELECT DISTINCT keszito.nev
    FROM keszito, kapcsolat
    WHERE keszito.id=kapcsolat.keszitoid
      AND kapcsolat.filmid IN
        (
        SELECT kapcsolat.filmid
        FROM kapcsolat, keszito
        WHERE keszito.id=kapcsolat.keszitoid
          AND nev="Clint Eastwood"
        )
      AND nev<>"Clint Eastwood";
      
SELECT kapcsolat.filmid
        FROM kapcsolat, keszito
        WHERE keszito.id=kapcsolat.keszitoid
          AND nev="Clint Eastwood";