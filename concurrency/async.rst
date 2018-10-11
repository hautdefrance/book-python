***********
Concurrency
***********

* Promises and Futures
* ``yield from``
* ``asyncio``
* ``async``/``await``
* Twisted, Tornado
* Curio, Trio

High-Level Concurrency
======================

* CPU-bound Concurrency:

    * Using Queues and Multiprocessing
    * Using Futures and Multiprocessing

* I/O-bound Concurrency:

    * Using Queues and Threading
    * Using Futures and Threading

Coroutine
=========

The word "coroutine", like the word "generator", is used for two different (though related) concepts:

- The function that defines a coroutine (a function definition using async def or decorated with ``@asyncio.coroutine``). If disambiguation is needed we will call this a coroutine function (``iscoroutinefunction()`` returns ``True``).

- The object obtained by calling a coroutine function. This object represents a computation or an I/O operation (usually a combination) that will complete eventually. If disambiguation is needed we will call it a coroutine object (``iscoroutine()`` returns ``True``).

``Asyncio``
===========

Protocol
--------
* ``__await__``
* ``__aiter__``, ``__anext__``
* ``__aenter__``, ``__aexit__``

.. code-block:: python

    class Reader:
        async def readline(self):
            ...

        def __aiter__(self):
            return self

        async def __anext__(self):
            val = await self.readline()
            if val == b'':
                raise StopAsyncIteration
            return val

.. code-block:: python

    class AsyncContextManager:
        async def __aenter__(self):
            await log('entering context')

        async def __aexit__(self, exc_type, exc, tb):
            await log('exiting context')

Low-level API
-------------
- callbacks
- Transport and Protocols
- network, subprocesses, signals

``async``/``await``
-------------------
- run coroutines
- streams, sockets, subprocesses, locks, timeouts, cancelations

Mainstream
----------
- in standard library since Python 3.5
- stable and supported
- healthy ecosystem
- HTTP: aiohttp, Sanic
- DBs: asyncpg, aio-libs, aiomysql

Pluggable event loop
--------------------
- uvloop - makes asyncio 2-4x faster
- PyO3

.. code-block:: python

    loop = asyncio.get_event_loop()
    loop.create_task()
    loop.run_until_complete()
    loop.run_forever()

    asyncio.geather()
    loop.run_in_executor()

Przykłady praktyczne
====================

Hello World coroutine
---------------------
.. code-block:: python

    import asyncio

    async def hello_world():
        print("Hello World!")

    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    loop.run_until_complete(hello_world())
    loop.close()

Coroutine displaying the current date
-------------------------------------
.. code-block:: python

    import asyncio
    import datetime

    async def display_date(loop):
        end_time = loop.time() + 5.0
        while True:
            print(datetime.datetime.now())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)

    loop = asyncio.get_event_loop()
    # Blocking call which returns when the display_date() coroutine is done
    loop.run_until_complete(display_date(loop))
    loop.close()

Chain coroutines
----------------
.. code-block:: python

    import asyncio

    async def compute(x, y):
        print("Compute %s + %s ..." % (x, y))
        await asyncio.sleep(1.0)
        return x + y

    async def print_sum(x, y):
        result = await compute(x, y)
        print("%s + %s = %s" % (x, y, result))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()

Future with ``run_until_complete()``
------------------------------------
.. code-block:: python

    import asyncio

    async def slow_operation(future):
        await asyncio.sleep(1)
        future.set_result('Future is done!')

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))
    loop.run_until_complete(future)
    print(future.result())
    loop.close()

Parallel execution of tasks
---------------------------
.. code-block:: python

    import asyncio

    async def factorial(name, number):
        f = 1
        for i in range(2, number+1):
            print("Task %s: Compute factorial(%s)..." % (name, i))
            await asyncio.sleep(1)
            f *= i
        print("Task %s: factorial(%s) = %s" % (name, number, f))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    ))
    loop.close()
