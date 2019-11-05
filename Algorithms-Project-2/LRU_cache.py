class LRU_Cache(object):

    def __init__(self, capacity):
        self.list = [None for _ in range(capacity)]
        print(self.list)

        pass

    def get(self, key):

        if self.list[key] is not True:
            return -1
        else:
            return self.list[key]

        pass

    def set(self, key, value):
        self.list[key] = value
        print(self.list[key])
        
    def cache_hit():
        if self.get() is True:


our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2

our_cache.set(5, 5) 
our_cache.set(6, 6)
