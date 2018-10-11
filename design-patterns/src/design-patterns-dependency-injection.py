from datetime import timedelta


class Cache:
    def __init__(self, expiration=timedelta(days=30), location=None):
        self.expiration = expiration
        self.location = location

    def get(self):
        raise NotImplementedError

    def set(self):
        raise NotImplementedError

    def is_valid(self):
        raise NotImplementedError


class CacheFilesystem(Cache):
    """Cache using files"""


class CacheMemory(Cache):
    """Cache using memory"""


class CacheDatabase(Cache):
    """Cache using database"""


class HTTP:
    def __init__(self, cache):
        # Inject Cache object
        self._cache = cache

    def _fetch(self, url):
        return ...

    def get(self, url):
        if self._cache.is_valid():
            # Use cached data
            self._cache.get(url)
        else:
            data = self._fetch(url)
            self._cache.set(url, data)


if __name__ == '__main__':
    database = CacheDatabase(location='sqlite3://http-cache.sqlite3')
    filesystem = CacheFilesystem(location='/tmp/http-cache.txt')
    memory = CacheMemory(expiration=timedelta(hours=2))

    http1 = HTTP(cache=database)
    http1.get('http://python.astrotech.io')

    http2 = HTTP(cache=filesystem)
    http2.get('http://python.astrotech.io')

    http3 = HTTP(cache=memory)
    http3.get('http://python.astrotech.io')
