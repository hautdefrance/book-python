UPDATE kontakty SET
    first_name='José'
  WHERE last_name='Jiménez';


UPDATE kontakty SET
    first_name=:firstname,
    last_name=:lastname,
    address=:address
WHERE id=:id
