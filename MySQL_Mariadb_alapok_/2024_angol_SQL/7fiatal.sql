/*7. Lekérdezés segítségével adja meg azon királyok nevét, akik 15 évesnél fiatalabban kezdtek
uralkodni, és hogy ekkor hány évesek voltak! Az adatokat az életkor szerint növekvő
sorrendben jelenítse meg! (7fiatal)*/
SELECT uralkodo.nev, uralkodo.hal-uralkodo.szul as kor, uralkodo.szul-hivatal.mettol  FROM uralkodo, hivatal
WHERE uralkodo.hal-uralkodo.szul <= 15 and uralkodo.szul-hivatal.mettol <=15
ORDER by kor ASC;
