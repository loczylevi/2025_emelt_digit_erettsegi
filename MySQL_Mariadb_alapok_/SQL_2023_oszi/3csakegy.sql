/*3. A feladatsor táblát használva, lekérdezés segítségével jelenítse meg a feladatsor
névadójának nevét, ha abban pontosan egy szóköz van! (3csakegy)*/

SELECT feladatsor.nevado FROM feladatsor WHERE feladatsor.nevado LIKE "% %" AND feladatsor.nevado NOT LIKE "% % %";
