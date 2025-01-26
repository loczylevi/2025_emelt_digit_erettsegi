# 2025_emelt_digit_erettsegi

## minden feladat a következő linken elérhető:
### források:

https://emelt.sulipy.hu/

https://sulipy.hu/

https://www.oktatas.hu/kozneveles/erettsegi/feladatsorok

https://sql.sulipy.hu/

## ami eddig kész python programozás :white_check_mark: 

https://dload-oktatas.educatio.hu/erettsegi/feladatok_2024osz_emelt/e_digkult_24okt_fl.pdf
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2024tavasz_emelt/e_digkultma_24maj_fl.pdf
https://dload-oktatas.educatio.hu/erettsegi/feladatok_2024tavasz_emelt/e_digkult_24maj_fl.pdf

## ami eddig kész SQL programozás :white_check_mark: 

_nothing_ broo 	(づ ◕‿◕ )づ

mind megbukunk let's goooo xd

```sql
--- forrás:  https://sql.sulipy.hu/sql2/fuggvenyek?tab=feladatok

SELECT * FROM `products` WHERE 1     -- ૮₍ ˶•⤙•˶ ₎ა

                                             ---|||--- SQL Függvények Feladatok --|||---
-- UwU
/*1. Feladat
A 'products' táblában határozd meg a 'standard_cost' mezőjének átlagértékét
a, az össezs rekord esetében,
b, azon rekordok esetében, amelyeknél a 'list_price' 30-nál kisebb értékű,
c, azon rekordok esetében, amelyeknél a 'category' mezőben 'Sauces' érték található!*/


SELECT AVG(standard_cost) AS atlag_ertek FROM products;

SELECT AVG(standard_cost) AS atlag_ertek_2 FROM products WHERE list_price < 30;

SELECT *  FROM products WHERE list_price < 30;

SELECT AVG(standard_cost) AS atlag_ertek_3 FROM products WHERE category LIKE "%Sauces%";

SELECT * FROM products WHERE category LIKE "%Sauces%";

SELECT * FROM products WHERE category = "Sauces";

SELECT * FROM products WHERE category IN ("Sauces");

/*2. Feladat
A 'products' táblában határozd meg a 'standard_cost' mezőjének összértékét
a, az össezs rekord esetében,
b, azon rekordok esetében, amelyeknél a 'list_price' értéke 20 és 50 közötti,
c, azon rekordok esetében, amelyeknél a 'category' mezőben NEM 'Sauces' érték található!
*/


SELECT SUM(standard_cost) AS ossz_ertek_1 FROM products;

SELECT SUM(standard_cost) AS ossz_ertek_2 FROM products WHERE list_price BETWEEN 20 AND 50;

SELECT * FROM products WHERE list_price BETWEEN 20 AND 50;

SELECT * FROM products WHERE 20 < list_price AND list_price < 50;

SELECT SUM(standard_cost) AS ossz_erte_3 FROM products WHERE category <> "Sauces";

SELECT * FROM products WHERE category <> "Sauces";

/*
3. Feladat
A 'employees' táblában határozd meg azon alkalmazottak számát
a, akik Seattle-ben laknak,
b, akiknek 'Sales Representative' munkakörben dolgoznak
c, akiknek a keresztneve 'A' betűvel kezdődik!
*/

SELECT COUNT(id) AS szamlalo_1 FROM employees WHERE city = "Seattle";

SELECT * FROM employees WHERE city = "Seattle";

SELECT * FROM employees WHERE city IN ("Seattle");

SELECT * FROM employees WHERE city LIKE "%Seattle%";

SELECT COUNT(id) AS szamlalo_2 FROM employees WHERE job_title = "Sales Representative";

SELECT * FROM employees WHERE job_title = "Sales Representative";

SELECT * FROM employees WHERE job_title LIKE "%Sales Representative%";

SELECT * FROM employees WHERE job_title IN ("Sales Representative");

SELECT COUNT(id) AS szamlalo_3 FROM employees WHERE first_name LIKE "a%";

SELECT first_name FROM employees WHERE first_name LIKE "a%";


/*
4. Feladat
A 'products' táblában határozd meg a 'standard_cost' oszlop
a, legkisebb értékét,
b, legnagyobb értékét,
c, legnagyobb értékét, azon rekordok esetében, ahol a 'list_price' legalább 30,
d, legnagyobb értékét, azon rekordok esetében, ahol a 'product_code' tartalmazza a 'CO' sztringet!
*/

SELECT MIN(standard_cost) AS legkisebb FROM products;

SELECT MAX(standard_cost) AS legnagyobb FROM products;

SELECT MAX(standard_cost) AS legnagyobb_feltetellel_1 FROM products WHERE list_price >= 30;

SELECT MAX(standard_cost) AS legnagyobb_feltetellel_2 FROM products WHERE product_code LIKE "%CO%";

SELECT product_code,standard_cost FROM products WHERE product_code LIKE "%CO%";

SELECT list_price,standard_cost FROM products WHERE list_price >= 30;

SELECT standard_cost FROM products ORDER BY standard_cost ASC;

SELECT standard_cost FROM products ORDER BY standard_cost DESC;

-- ૮₍ ˶•⤙•˶ ₎ა
```
