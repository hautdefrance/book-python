UPDATE kontakty SET firstname='José' WHERE lastname='Jiménez';

UPDATE kontakty SET
    firstname=:firstname,
    lastname=:lastname,
    adresy=:adresy
WHERE id=:id
