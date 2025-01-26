USE northwind;

--                                                        ---|||---  SQL FÜGGVÉNYEK  ---|||---

-- SELECT * from customers WHERE first_name LIKE "E%";
-- DESCRIBE products;
-- SELECT MIN(Type) FROM products;

SELECT MIN(list_price) AS legolcsobb FROM products;

SELECT MAX(list_price) AS legdragabb FROM products;

SELECT * FROM products ORDER BY list_price ASC;

SELECT * FROM products ORDER BY list_price DESC;

SELECT COUNT(description) AS szamlalo FROM products WHERE description IS NOT NULL;

SELECT COUNT(id) AS szamlalo2 FROM products WHERE list_price = 1.2;

SELECT * FROM products ORDER BY list_price ASC;

SELECT SUM(list_price) AS osszesen FROM products;

SELECT SUM(list_price) AS osszesen_feltetellel FROM products WHERE  id < 4;

SELECT * FROM products WHERE id < 4;

SELECT AVG(list_price) AS atlag FROM products WHERE id < 4;
