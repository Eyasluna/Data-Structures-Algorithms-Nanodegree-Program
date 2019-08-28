'''
Design a a data structure for a Least Recently Used (LRU) cache with O(1) operations.
It holds most recently used items while staying memory constrained. Specifically, the LRU cache removes recently used items when low on memory or capacity.
It to support two operations, get and set
The get operation should retrieve the value if the key exists, otherwise it should return -1 if it does not exist.
The set operation will insert the value if the key is not present. If the cache is full then it should remove the oldest item before inserting a new item.
'''
from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        try:  # If value in the cache

            # Update priority due to access
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        if key in self.cache:  # Update priority due to access
            self.cache.pop(key)
            self.cache[key] = value

        else:  # Add to cache
            if len(self.cache) < self.capacity:  # Still space on cache
                self.cache[key] = value

            else:  # No space available on cache
                self.cache.popitem(last=False)
                self.cache[key] = value

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