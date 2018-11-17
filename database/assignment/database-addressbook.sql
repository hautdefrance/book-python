CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created DATETIME,
    modified DATETIME,
    first_name TEXT,
    last_name TEXT,
    date_of_birth DATE
);

CREATE UNIQUE INDEX IF NOT EXISTS last_name_index ON contact (last_name);
CREATE INDEX IF NOT EXISTS modified_index ON contact (modified);

CREATE TABLE IF NOT EXISTS address (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id INTEGER,
    street TEXT,
    city TEXT,
    state TEXT,
    code INT,
    country TEXT
);

INSERT INTO contact VALUES (
    NULL,
    :created,
    :modified,
    :first_name,
    :last_name,
    :date_of_birth
);

INSERT INTO address VALUES (
    NULL,
    :contact_id
    :street,
    :city,
    :state,
    :code,
    :country
);

UPDATE contact SET
    first_name=:firstname,
    last_name=:lastname,
    modified=:modified
WHERE id=:id;

SELECT * FROM contact;
