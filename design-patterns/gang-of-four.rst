************
Gang of Four
************


Examples
========
* https://www.toptal.com/python/python-design-patterns


Singleton
---------
.. literalinclude:: src/design-patterns-singleton.py
    :language: python
    :caption: Singleton Design Pattern

Gateway
-------
.. literalinclude:: src/design-patterns-gateway.py
    :language: python
    :caption: Gateway Design Pattern

Factory
-------
.. literalinclude:: src/design-patterns-factory-1.py
    :language: python
    :caption: Factory Design Pattern

.. literalinclude:: src/design-patterns-factory-2.py
    :language: python
    :caption: Factory Design Pattern

Dependency Injection
--------------------
.. literalinclude:: src/design-patterns-dependency-injection.py
    :language: python
    :caption: Dependency Injection Design Pattern

Callback
--------
.. literalinclude:: src/design-patterns-callback.py
    :language: python
    :caption: Callback Design Pattern

State Machine
-------------
* StateMachine imposes a structure to automatically change the implementation from one object to the next
* The current implementation represents the state that a system is in
* System behaves differently from one state to the next
* The code that moves the system from one state to the next
* Each state can be ``run()`` to perform its behavior
* You can pass it an ``input`` object so it can tell you what new state to move to based on that ``input``
* Each State object decides what other states it can move to, based on the ``input``
* Each State object has its own little State table
* There is a single master state transition table for the whole system

.. code-block:: text

    statemachine TrafficLight:
        Red -> Green
        Green -> Amber
        Amber -> Red


    Red.wait = sleep(2)
    Amber.wait = sleep(1)
    Green.wait = sleep(2)


.. literalinclude:: src/design-patterns-state-machine.py
    :language: python
    :caption: State Machine


Structural Design Patterns
==========================
- Adapter (klasowy i obiektowy)
- Most (ang. Bridge) (obiektowy)
- Kompozyt (ang. Composite) (obiektowy)
- Dekorator (ang. Decorator) (obiektowy)
- Fasada (ang. Façade) (obiektowy)
- Pyłek (ang. Flyweight) (obiektowy)
- Pełnomocnik (ang. Proxy) (obiektowy)


Creational Design Patterns
==========================
- Metoda wytwórcza (ang. Factory Method) (klasowy)
- Fabryka Abstrakcyjna (ang. Abstract Factory) (obiektowy)
- Budowniczy (ang. Builder) (obiektowy)
- Prototyp (ang. Prototype) (obiektowy)
- Singleton (obiektowy)


Behavioral Design Patterns
==========================
- Łańcuch zobowiązań (ang. Chain of Responsibility) (obiektowy)
- Polecenie (ang. Command) (obiektowy)
- Interpreter (ang. Interpreter) (klasowy)
- Interator (obiektowy)
- Mediator (ang. Mediator) (obiektowy)
- Pamiątka (ang. Memento) (obiektowy)
- Obserwator (ang. Observer) (obiektowy)
- Stan (ang. State) (obiektowy)
- Strategia (ang. Strategy) (obiektowy)
- Metoda szablonowa (ang. Template Method) (klasowy)
- Odwiedzający (ang. Visitor) (obiektowy)


Idiomy języka programowania
===========================
- Wzorzec EFAP (ang. It's easier to ask for forgiveness than permission)
- Wzorzec Metaklasy
- Borg
- Klasa domieszkowa w języku Python (ang. Mixin)
