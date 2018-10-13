CREATE DATABASE databasename;


CREATE TABLE IF NOT EXISTS kontakty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pesel INTEGER UNIQUE,
    firstname TEXT,
    lastname TEXT
)

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);

CREATE TABLE people (
    id integer primary key auto increment,
    first_name varchar(20),
    last_name varchar(20)
);

CREATE TABLE IF NOT EXISTS sensor_data (
    datetime DATETIME PRIMARY KEY,
    sync_datetime DATETIME DEFAULT NULL,
    device VARCHAR(255),
    parameter VARCHAR(255),
    value REAL,
    unit VARCHAR(255)
);

CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;