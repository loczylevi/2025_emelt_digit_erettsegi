/*3. Készítsen lekérdezést, amely felsorolja az Árpád-ház tagjainak nevét, uralkodásuk kezdő és
befejező évét az uralkodásuk sorrendjében! Ha valaki többször uralkodott, akkor a listában
többször jelenjen meg! (3arpad) */

SELECT uralkodo.nev, hivatal.mettol, hivatal.meddig FROM hivatal, uralkodo,uralkodohaz
WHERE hivatal.uralkodo_az = uralkodo.azon and uralkodo.uhaz_az = uralkodohaz.azon AND uralkodohaz.nev = "Árpád-ház";

