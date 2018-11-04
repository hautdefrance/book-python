.. _SQL:

***
SQL
***


ACID
====
* Atomicity
* Consistency
* Isolation
* Durability

Atomicity
---------
Transactions are often composed of multiple statements. Atomicity guarantees that each transaction is treated as a single "unit", which either succeeds completely, or fails completely: if any of the statements constituting a transaction fails to complete, the entire transaction fails and the database is left unchanged. An atomic system must guarantee atomicity in each and every situation, including power failures, errors and crashes.

Consistency
-----------
Consistency ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants: any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof. This prevents database corruption by an illegal transaction, but does not guarantee that a transaction is correct.

Isolation
---------
Transactions are often executed concurrently (e.g., reading and writing to multiple tables at the same time). Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially. Isolation is the main goal of concurrency control; depending on the method used, the effects of an incomplete transaction might not even be visible to other transactions.

Durability
----------
Durability guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure (e.g., power outage or crash). This usually means that completed transactions (or their effects) are recorded in non-volatile memory.



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

COMMIT and ROLLBACK
===================
.. literalinclude:: src/sql-commit-rollback.sql
    :language: sql
    :caption: COMMIT and ROLLBACK

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
