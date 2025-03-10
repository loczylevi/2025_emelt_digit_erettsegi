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
VALUES (77, 'Szego Pal', 'Continental', 'Budapest', '8', 99, '2022-01-05');

INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (101, 'Horvath Tamas', 'PEMÜ', 'Szeged', '9', 21, '2022-01-05');

INSERT INTO customers (customer_id, name, ceg, varos, special_azo, free_Vbuck, szuletes) 
VALUES (102, 'Szabo Nora', 'BKV', 'Pozsony', '69funynumberGOBRRRRR', 77, '2022-01-05');

-- Inserting orders (No changes needed)
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1000, '2022-01-05', 1);
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1001, '2022-01-07', 2);
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1002, '2022-02-03', 77);
INSERT INTO orders (order_id, order_date, customer_id) VALUES (1003, '2022-01-09', 77);


SELECT * FROM customers;
ALTER TABLE orders DROP CONSTRAINT FK_customer_order ;  -- a kapcsolat megszüntetése a szülő és gyermek táblázat között
ALTER TABLE orders ADD CONSTRAINT FK_customer_order FOREIGN KEY (customer_id) REFERENCES customers (customer_id); -- a kapcsolat létrehozása a szülő és gyermek táblázat között
