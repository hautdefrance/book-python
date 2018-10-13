.. _SQL:

***
SQL
***

Data Types
==========
.. csv-table:: SQLite data types
    :header-rows: 1
    :file: data/sql-types.csv

Constrains
==========
.. csv-table:: SQL Constraints
    :header-rows: 1
    :file: data/sql-constraints.csv

CREATE
======
.. literalinclude:: src/sql-create.sql
    :language: sql
    :caption: CREATE

INSERT
======
.. literalinclude:: src/sql-insert.sql
    :language: sql
    :caption: INSERT

SELECT
======
.. literalinclude:: src/sql-select.sql
    :language: sql
    :caption: SELECT

AUTOINCREMENT
=============
.. literalinclude:: src/sql-autoincrement.sql
    :language: sql
    :caption: Auto Increment

UPDATE
======
.. literalinclude:: src/sql-update.sql
    :language: sql
    :caption: UPDATE

GROUP BY
========
.. literalinclude:: src/sql-group.sql
    :language: sql
    :caption: GROUP BY

HAVING
======
.. literalinclude:: src/sql-having.sql
    :language: sql
    :caption: HAVING

ALTER
=====
.. literalinclude:: src/sql-alter.sql
    :language: sql
    :caption: ALTER

DROP
====
* https://www.youtube.com/watch?v=1aEqd4bl6Bs
* write your statement starting with ``--``
* after you're sure, remove comments

.. literalinclude:: src/sql-drop.sql
    :language: sql
    :caption: DROP

DELETE
======
* write your statement starting with ``--``
* after you're sure, remove comments

.. literalinclude:: src/sql-delete.sql
    :language: sql
    :caption: DELETE

JOIN
====

INNER JOIN
----------
.. figure:: img/sql-innerjoin.gif
    :align: center
    :scale: 100%

LEFT JOIN
---------
.. figure:: img/sql-leftjoin.gif
    :align: center
    :scale: 100%

RIGHT JOIN
----------
.. figure:: img/sql-rightjoin.gif
    :align: center
    :scale: 100%

FULL JOIN
---------
.. figure:: img/sql-fulljoin.gif
    :align: center
    :scale: 100%

JOIN
----
.. literalinclude:: src/sql-join.sql
    :language: sql
    :caption: JOIN

TRUNCATE
========
.. literalinclude:: src/sql-truncate.sql
    :language: sql
    :caption: TRUNCATE

SQL Injection
=============
.. literalinclude:: src/sql-injection.py
    :language: python
    :caption: SQL Injection
