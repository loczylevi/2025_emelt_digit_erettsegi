DROP DATABASE IF EXISTS muhely;
CREATE DATABASE muhely;
USE muhely;

CREATE TABLE szgk(
    id INT,
    tipus VARCHAR(20),
    modell VARCHAR(20),
    rendszam VARCHAR(20),
    ajtok_szama INT,
    gyartas_eve DATE
);

INSERT INTO szgk(tipus,modell,rendszam,ajtok_szama, gyartas_eve) VALUES("Skoda", "Opel","LOL345",4,"1972-04-30");
