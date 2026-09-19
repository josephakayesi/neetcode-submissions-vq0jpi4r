"""
Intuition
- We keep a cache that stores values in our cache. 
- Anytime we use a put and a get; we need to move that item to the front as the most recently used. 
- Naturally items that are lest recently used with be pushed to the back of the cache*

Consider keeping a queue to find the least recently used. 

cache = {
3=30,
    2=20
}
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        self.cache.move_to_end(key, last=True)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)

        # Check if cache is full
        if len(self.cache) > self.capacity:
            # Remove the least recently used and insert the new items
            self.cache.popitem(last=False) 



        
