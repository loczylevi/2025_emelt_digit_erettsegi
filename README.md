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

## Xamp inditása terminálból ubuntun
```bash
sudo /opt/lampp/manager-linux-x64.run
```
# SQL PUSKA
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

# SQL PUSKA UNION | GROUP BY | HAVING
```sql
/*
1. Feladat
Az orders tábla ship_state_province mezőjének értékeit fésüld össze a customers tábla state_province mezőjének értékeivel úgy, hogy
- minden érték csak egyszer szerepeljen,
- az értékek ismétlődhetnek!
*/


SELECT ship_state_province FROM orders
UNION 
SELECT state_province FROM customers;


SELECT ship_state_province FROM orders
UNION ALL
SELECT state_province FROM customers;


/*
2. Feladat
A products táblában számold meg kategóriánként (category mező) a termékek számát!
*/

SELECT COUNT(category) as db, category FROM products
GROUP BY category;

SELECT COUNT(category) AS szamlalo FROM products WHERE category = "Baked Goods & Mixes";

SELECT COUNT(category) AS szamlalo2 FROM products WHERE category = "Canned Fruit & Vegetables";


/*
3. Feladat
A orders táblában számold meg városonként (ship_city mező) a rendelések számát!
*/

SELECT COUNT(ship_city) AS rendelesek_szama, ship_city FROM orders
GROUP BY ship_city;

SELECT COUNT(ship_city) FROM orders WHERE ship_city = "Chicago";

/*
4. Feladat
A customers táblából kérd le az ügyfelek számát városonként, ha az eléri legalább a 3-at!
*/
SELECT COUNT(id), city from customers
GROUP BY city;

SELECT COUNT(id) AS ugyfelek_szama, city from customers
GROUP BY city
HAVING COUNT(id) >= 3;
```
## CREATE és FOREIGN KEY 
```sql
DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;

-- Parent Table: Customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(40),
    ceg VARCHAR(40) DEFAULT "WESKO szakkör",
    varos VARCHAR(20) NOT NULL,
    special_azo VARCHAR(20) UNIQUE,
    free_Vbuck INT CHECK(free_Vbuck < 100),  -- akinek több Vbuckja van mint 100 az CSAL!!4!!4!!!
    szuletes DATE
);

-- Child Table: Orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    CONSTRAINT FK_customer_order 
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

-- Data Insertion (Fixing column name and structure)
INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (1, 'Czikybors Flóra', 'CC KFT', 'MISKOLC', '4', 99, '2028-01-05');

INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (2, 'Perie Banzsai', 'Szalézi KFT', 'DEBRECEN', '7', 88, '2022-01-05');  

INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (77, 'Vlagyimir Szergejovics Ivel Puskin', 'Continental', 'Budapest', '8', 99, '2022-01-05');

INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (101, 'Candide', 'PEMÜ', 'Szeged', '9', 21, '2022-01-05');

INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (102, 'Voltaire', 'BKV', 'Pozsony', '69funynumberGOBRRRRR', 77, '2022-01-05');

-- Inserting orders (No changes needed)
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1000, '2022-01-05', 1);
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1001, '2022-01-07', 2);
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1002, '2022-02-03', 77);
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1003, '2022-01-09', 77);


SELECT * FROM customers;
ALTER TABLE orders DROP CONSTRAINT FK_customer_order ;  -- a kapcsolat megszüntetése a szülő és gyermek táblázat között
ALTER TABLE orders ADD CONSTRAINT FK_customer_order FOREIGN KEY (customer_id) REFERENCES customers (customer_id); -- a kapcsolat létrehozása a szülő és gyermek táblázat között
```
# SQL PUSKA JOIN | INNER | LEFT | RIGHT | SELF | CROSS nyunyor xd
```sql

DROP DATABASE IF EXISTS klanok;
CREATE DATABASE klanok;
USE klanok;

CREATE TABLE P_ACE(
    id INT AUTO_INCREMENT PRIMARY KEY,
    klan VARCHAR(10) DEFAULT "P-ACE",
    jatekos VARCHAR(30),
    tank VARCHAR(30),
    loszer INT CHECK (loszer > 0),
    avg_dmg INT
    );
    
CREATE TABLE L1MIT(
    id INT AUTO_INCREMENT PRIMARY KEY,
    klan VARCHAR(10) DEFAULT "L1MIT",
    jatekos VARCHAR(30),
    tank VARCHAR(30),
    loszer INT CHECK (loszer > 0),
    avg_dmg INT
    
);

INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("kiki","liberte",52,2000);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("tjoe","defender",47,1000);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("destex","progetto46",60,1500);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("trapi","BZ-176",40,2500);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("zsolt","KV-4",70,3000);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("szikkadt","BZ-176",70,800);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("Mate","BZ-176",70,800);

INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Vencel_The_champion","BZ-176",52,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("NK","BZ-176",47,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("NK_the_p@rnstar","Obj 252u",60,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Tfce","Miel",40,4500);

INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Hunor_Magyar_77","703",52,2400);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Marcsellino","BZ-176",47,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM2","Obj 252u",60,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM3","SKODA T56",40,4500);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM4","Renegade",40,4500);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM5","BZ-1767",40,4500);

-- SELECT * FROM P_ACE;

-- SELECT * FROM L1MIt;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
INNER JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
LEFT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
RIGHT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
CROSS JOIN L1MIT;

SELECT *
FROM P_ACE
INNER JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT *
FROM P_ACE
LEFT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT *
FROM P_ACE
RIGHT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;
```
