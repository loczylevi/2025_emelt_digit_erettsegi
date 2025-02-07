DROP DATABASE IF EXISTS klanok;
CREATE DATABASE klanok;
USE klanok;

-- DROP TABLE IF EXISTS P_ACE;

CREATE TABLE P_ACE(
    id INT AUTO_INCREMENT PRIMARY KEY,
    klan VARCHAR(10) DEFAULT "P-ACE",
    jatekos VARCHAR(30),
    tank VARCHAR(30),
    loszer INT CHECK (loszer > 0),
    avg_dmg INT
    );
    
-- DROP TABLE IF EXISTS L1MIT;

CREATE TABLE L1MIT(
    id INT AUTO_INCREMENT PRIMARY KEY,
    klan VARCHAR(10) DEFAULT "L1MIT",
    jatekos VARCHAR(30),
    tank VARCHAR(30),
    loszer INT CHECK (loszer > 0),
    avg_dmg INT
    
);

INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("kiki","liberte",52,2000);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("tjoe","defender",47,1000);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("destex","progetto46",60,1500);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("trapi","BZ-176",40,2500);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("zsolt","KV-4",70,3000);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("szikkadt","BZ-176",70,800);
INSERT INTO P_ACE (jatekos,tank,loszer,avg_dmg) VALUES ("Mate","BZ-176",70,800);

INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Vencel_The_champion","BZ-176",52,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("NK","BZ-176",47,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("NK_the_p@rnstar","Obj 252u",60,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Tfce","Miel",40,4500);

INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Hunor_Magyar_77","703",52,2400);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("Marcsellino","BZ-176",47,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM2","Obj 252u",60,4000);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM3","SKODA T56",40,4500);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM4","Renegade",40,4500);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM5","BZ-1767",40,4500);
INSERT INTO L1MIT (jatekos,tank,loszer,avg_dmg) VALUES ("MAJOM6","BZ-1767",40,4500);


-- SELECT * FROM P_ACE;

-- SELECT * FROM L1MIt;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
INNER JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
LEFT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
RIGHT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT P_ACE.jatekos AS A_GAMER, P_ACE.klan AS A_CLAN, P_ACE.tank AS tonk, L1MIT.jatekos AS B_GAMER, L1MIT.klan AS B_CLAN
FROM P_ACE
CROSS JOIN L1MIT;

SELECT *
FROM P_ACE
INNER JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT *
FROM P_ACE
LEFT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT *
FROM P_ACE
RIGHT JOIN L1MIT
ON P_ACE.tank = L1MIT.tank;

SELECT *
FROM P_ACE
CROSS JOIN L1MIT;
