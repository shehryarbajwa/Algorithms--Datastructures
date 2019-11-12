class Node:

    def __init__(self, key, value):
        self.previous = None
        self.next = None
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity):
        self.capactiy = capacity
        self.dictionary = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key):
        if key in self.dictionary:
            n = self.dictionary[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def set(self, key, value):
        if key in self.dictionary:
            self._remove(self.dictionary[key])
        n = Node(key, value)
        self._add(n)
        self._remove(n)
        self.dictionary[key] = n

        if len(self.dictionary) > self.capactiy:
            n = self.head.next
            self._remove(n)
            del self.dictionary[n.key]

    def _remove(self, node):
        previous = node.previous
        _next = node.next
        previous.next = _next
        _next.previous = previous

    def _add(self, node): 
        previous = self.tail.previous
        previous.next = node
        self.tail.previous = node
        node.previous = previous
        node.next = self.tail

#Test cases
new_cache = LRUCache(5)

new_cache.set(1,1)
new_cache.set(2,1)
new_cache.set(3,1)
new_cache.set(4,1)
new_cache.set(5,1)

print(new_cache.get(4))
#Answer is 1
#Test case 2

cache_2 = LRUCache(4)
cache_2.set(1,2)
cache_2.set(2,2)
cache_2.set(3,2)
cache_2.set(4,2)

print(cache_2.get(4))
#Answer is 2
#Test case 3
cache_3 = LRUCache(6)
cache_3.set(1,5)
cache_3.set(2,6)
cache_3.set(3,7)
cache_3.set(4,8)

print(cache_3.get(4))
#Answer is 8

