-- https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

/*1. Feladat
Írj SQL utasítást amely az online tesztadatbázis 'Categories' táblájából lekérdezi
a, az összes adatot,
b, a 'CategoryName' oszlopba tartozó adatokat,
c, a 'CategoryName' és 'Description' oszlopba tartozó adatokat!*/

SELECT * FROM Categories;

SELECT CategoryName FROM Categories;

SELECT CategoryName,Descriptio FROM Categories;

/*2. Feladat
Írj SQL utasítást amely az online tesztadatbázis 'Products' táblájából lekérdezi
a, a 'ProductName', 'Unit' és 'Price' oszlopba tartozó adatokat,
b, azon termékek nevét és árát, amelyek ára 20-nál kevesebb,
c, azon termékek nevét és árát, amelyek ára 20 és 30 közé esik,
d, azon termékek nevét és árát, amelyek ára nem 10,
e, a 'T' betűvel kezdődő temékek nevét,
f, azon termékek nevét, amelynek neve a 'Louisiana' szóval kezdődik!*/

SELECT * FROM Products;

SELECT ProductName,Unit,Price FROM Products;

SELECT ProductName,Price FROM Products WHERE Price < 20;

SELECT ProductName,Price FROM Products WHERE Price BETWEEN 20 AND 30;

SELECT ProductName,Price FROM Products WHERE 20 < Price AND Price < 30;

SELECT ProductName,Price FROM Products WHERE Price <> 10;

SELECT ProductName,Price FROM Products WHERE ProductName LIKE 'T%';

SELECT ProductName FROM Products WHERE ProductName LIKE 'Louisiana%';

/*3. Feladat
Írj SQL utasítást amely az online tesztadatbázis 'Suppliers' táblájából lekérdezi az országokat ismétlődés nélkül!*/

SELECT DISTINCT Country FROM Suppliers;
