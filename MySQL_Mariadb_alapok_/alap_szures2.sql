-- https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

/*1. Feladat
Írj SQL utasítást amely az online tesztadatbázis 'Categories' táblájából lekérdezi
a, az összes adatot,
b, a 'CategoryName' oszlopba tartozó adatokat,
c, a 'CategoryName' és 'Description' oszlopba tartozó adatokat!*/

SELECT * FROM Categories;

SELECT CategoryName FROM Categories;

SELECT CategoryName,Descriptio FROM Categories;

