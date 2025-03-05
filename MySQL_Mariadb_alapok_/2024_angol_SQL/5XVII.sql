/*5. Lekérdezés segítségével határozza meg, hogy hány király volt Magyarországon 1601-től
1700-ig! Vegye figyelembe, hogy a királyok uralkodásának csak egy része is eshetett
a megjelölt időszakba! Kihasználhatja, hogy ebben az időszakban minden király csak
egyszer uralkodott. (5XVII) */

SELECT COUNT(*), mettol, meddig FROM hivatal
WHERE 1601 < mettol AND mettol < 1700 and 1601 < meddig AND meddig < 1700;


