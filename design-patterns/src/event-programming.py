class event:
    __slots__ = ('__subscribers', )

    def __init__(self):
        self.__subscribers = set()

    def call(self, *args, **kwargs):
        for subscriber in self.__subscribers:
            subscriber(*args, **kwargs)
    __call__ = call

    def register(self, function):
        self.__subscribers.add(function)
        return self
    __add__ = __iadd__ = register

    def unregister(self, function):
        self.__subscribers.remove(function)
        return self
    __sub__ = __isub__ = unregister

class EventManager:
    @staticmethod
    def register(name):
        if not hasattr(EventManager, name):
            setattr(EventManager, name, event())
        return getattr(EventManager, name).register



@EventManager.register('on_foo')
def foo(*args, **kwargs):
    print('Args: ' + str(args), 'Kwargs: ' + str(kwargs))

def call_on_foo():
    EventManager.on_foo()
    EventManager.on_foo(1, 2, 3)
    EventManager.on_foo(a=1, b=2, c=3)
    EventManager.on_foo(1, 2, 3, a=1, b=2, c=3)

@EventManager.register('on_bar')
def bar():
    call_on_foo()

EventManager.on_bar()



EventManager.on_bar += funkcja
