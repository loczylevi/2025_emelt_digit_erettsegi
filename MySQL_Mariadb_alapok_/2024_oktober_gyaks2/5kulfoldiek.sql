/*5. Lekérdezés segítségével határozza meg, hogy a 2000-es év után a magyar egyesületeken
kívül mely országok klubjainak játékosai nyertek bajnoki címet Magyarországon! Minden
ország neve egyszer szerepeljen a listában! (5kulfoldiek)*/

SELECT DISTINCT egyesulet.orszag FROM bajnok,  egyesulet, jatekos
WHERE jatekos.id = bajnok.jatekos_id AND bajnok.egyesulet_id = egyesulet.id AND bajnok.ev > 2000 AND egyesulet.orszag <> "Magyarország";