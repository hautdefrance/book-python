************
Templatetags
************


Filters
=======
* lower
* upper
* title
* date
* default
* timezone
* custom filters

.. code-block:: django

    {% load tz %}

    {{ value|timezone:"Europe/Paris" }}

.. code-block:: django

    {% load tz %}

    {{ value|utc }}

.. code-block:: django

    {% load tz %}

    {{ value|localtime }}


Simple Tags
===========
* trans
* custom tags


Assignment tags
===============



Block tags
==========
* custom block tags

.. code-block:: django

    {% load tz %}

    {% localtime on %}
        {{ value }}
    {% endlocaltime %}

    {% localtime off %}
        {{ value }}
    {% endlocaltime %}

.. code-block:: django

    {% load tz %}

    {% timezone "Europe/Paris" %}
        Paris time: {{ value }}
    {% endtimezone %}

    {% timezone None %}
        Server time: {{ value }}
    {% endtimezone %}
