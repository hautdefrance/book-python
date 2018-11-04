CREATE TABLE astronauts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
);


INSERT INTO astronauts VALUES ("José", "Jiménez");
INSERT INTO astronauts (first_name, last_name) VALUES ("Max", "Peck");


SELECT * FROM astronauts;

-- 1|José|Jiménez
-- 2|Max|Peck
