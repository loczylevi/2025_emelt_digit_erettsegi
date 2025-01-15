DROP DATABASE IF EXISTS muhely;
CREATE DATABASE muhely;
USE muhely;

CREATE TABLE szgk(
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipus VARCHAR(20) DEFAULT "Toyota",
    modell VARCHAR(20) NOT NULL,
    rendszam VARCHAR(20) UNIQUE,
    ajtok_szama INT CHECK(ajtok_szama < 6),
    gyartas_eve DATE
);

INSERT INTO szgk(tipus,modell,rendszam,ajtok_szama, gyartas_eve) VALUES("Skoda", "Opel","LOL345",4,"1972-04-30");
INSERT INTO szgk(tipus,modell,rendszam,ajtok_szama, gyartas_eve) VALUES("Skoda", "Opel","LOL345",4,"1972-04-30");

SELECT * FROM szgk;
