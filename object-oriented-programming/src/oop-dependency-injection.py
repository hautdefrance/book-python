class Engine(object):
    """Example engine base class.

    Engine is a heart of every car. Engine is a very common term and could be
    implemented in very different ways.
    """


class GasolineEngine(Engine):
    """Gasoline engine."""


class DieselEngine(Engine):
    """Diesel engine."""


class ElectroEngine(Engine):
    """Electro engine."""


class Car(object):
    """Example car."""

    def __init__(self, engine):
        """Initializer."""
        self._engine = engine  # Engine is injected


if __name__ == '__main__':
    gasoline_car = Car(engine=GasolineEngine())
    diesel_car = Car(engine=DieselEngine())
    electro_car = Car(engine=ElectroEngine())
