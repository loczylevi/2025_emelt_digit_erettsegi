/*9. Készítsen lekérdezést, amely megadja, hogy az „irodalom” művészeti ághoz tartozó
feladatsorok közül melyeket kellett ugyanabban a hónapban beadni, mint amikor kitűzték?
Adja meg a feladatsorok névadóját! (9ugyanabban) */


SELECT feladatsor.nevado FROM feladatsor
WHERE feladatsor.ag = "irodalom" AND MONTH(feladatsor.kituzes) = MONTH(feladatsor.hatarido);

