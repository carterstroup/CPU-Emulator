import collections

CACHE_SIZE = 16

# This class implements the cache of the CPU.
class Cache:
    # The actual cache is implemented as a dequeue.
    # Inside of the dequeue we use tuples to "simulate" the faster response from the CPU since tuples are accessed faster.
    def __init__(self):
        self.cache = collections.deque(maxlen=CACHE_SIZE)
        self.flush_cache()

    # Repeatedly append to the cache to flush the cache
    def flush_cache(self):
        for i in range(CACHE_SIZE):
            self.cache.append(("", ""))

    def search_cache(self, memory_address):
        for i in range(CACHE_SIZE):
            if self.cache[i][0] == memory_address:
                return self.cache[i][1]
        return None

    def write_cache(self, memory_address, value):
        self.cache.append(tuple((memory_address, value)))