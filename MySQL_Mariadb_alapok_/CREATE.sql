INSERT INTO customers(last_name,first_name,company,city,email_address) VALUES("Gipsz", "Jakab", "Bezsonet","veszprém","loczxy2003@gmail.com");

SELECT * FROM `customers` WHERE city = "Veszprém";

UPDATE customers SET last_name = "Bedecsi", company = "Bezsonet" WHERE id = 1;

CREATE DATABASE muhely;
DROP DATABASE muhely;
