'''
Design a a data structure for a Least Recently Used (LRU) cache with O(1) operations.
It holds most recently used items while staying memory constrained. Specifically, the LRU cache removes recently used items when low on memory or capacity.
It to support two operations, get and set
The get operation should retrieve the value if the key exists, otherwise it should return -1 if it does not exist.
The set operation will insert the value if the key is not present. If the cache is full then it should remove the oldest item before inserting a new item.
'''
from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
       # Initialize class variables
       self.cache_cap = capacity
       self.cache_val = {}
       self.cache_order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if non existant.
        if key is None:
            return -1

        return self.cache_val.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.cache_cap == 0:
            print("Can't perform operations on 0 capacity cache")
            return
        if len(self.cache_order) >= self.cache_cap:
            del self.cache_val[self.cache_order.popleft()]
        self.cache_order.append(key)
        self.cache_val[key] = value


our_cache = LRU_Cache(0)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 2)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(our_cache.get(None))    # return -1
# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)



print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1