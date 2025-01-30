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


