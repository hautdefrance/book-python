*******
Signals
*******


Available signals
=================

Model signals
-------------
* ``django.db.models.signals.pre_init``
* ``django.db.models.signals.post_init``
* ``django.db.models.signals.pre_save``
* ``django.db.models.signals.post_save``
* ``django.db.models.signals.pre_delete``
* ``django.db.models.signals.post_delete``

M2m relations
-------------
* ``django.db.models.signals.m2m_changed``
* ``django.db.models.signals.class_prepared``

Migrations
----------
* ``django.db.models.signals.pre_migrate``
* ``django.db.models.signals.post_migrate``

Request
-------
* ``django.core.signals.request_started``
* ``django.core.signals.request_finished``
* ``django.core.signals.got_request_exception``

Test
----
* ``django.test.signals.setting_changed``
* ``django.test.signals.template_rendered``

Database
--------
* ``django.db.backends.signals.connection_created``


Examples
========

.. code-block:: python

    from django.db.models.signals import pre_save
    from django.dispatch import receiver
    from myapp.models import MyModel


    @receiver(pre_save, sender=MyModel)
    def my_handler(sender, **kwargs):
        ...

.. code-block:: python

    from django.apps import AppConfig
    from django.db.models.signals import post_migrate

    def my_callback(sender, **kwargs):
        # Your specific logic here
        pass

    class MyAppConfig(AppConfig):
        ...

        def ready(self):
            post_migrate.connect(my_callback, sender=self)
