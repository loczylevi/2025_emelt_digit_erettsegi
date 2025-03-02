/*
7. Lekérdezés segítségével adja meg, hogy mely szerepek megnevezésében fordul elő a „rab”
szórészlet valamelyik szó elején! A szerepek megnevezése több szóból állhat, például „Roy,
rabszolgaszállító”. A lekérdezés a szerepet, a szerepet alakító színész és a hangot kölcsönző
szinkronszínész nevét adja meg! (7rab) 
*/
-- szerep --> rab like

SELECT szinkron.szerep, szinkron.szinesz, szinkron.hang FROM szinkron
WHERE szinkron.szerep LIKE "rab%" OR szinkron.szerep LIKE "% rab%";