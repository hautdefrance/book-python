username = "' OR 1=1; DROP TABLE users -- "
password = '132'

sql_query = f"""

    SELECT *
    FROM users
    WHERE 'username'='{username}'
    AND 'password'='{password}'

"""

print(sql_query)
# SELECT id, username, email
# FROM users
# WHERE 'username'='' OR 1=1; DROP TABLE users -- '
# AND 'password'='132'