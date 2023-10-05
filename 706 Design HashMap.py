# esign a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# Steps
# 1. create a list of size 1000000
# 2. create a function to put a key and value into the list
# 3. create a function to get a value from the list
# 4. create a function to remove a key and value from the list

# time: O(1)
# space: O(1)
# runtime: 440 ms, faster than 52.66% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.7 MB, less than 5.04% of Python3 online submissions for Design HashMap.

class MyHashMap:
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.hashmap = [-1] * 1000000
            
    
        def put(self, key: int, value: int) -> None:
            """
            value will always be non-negative.
            """
            self.hashmap[key] = value
            
    
        def get(self, key: int) -> int:
            """
            Returns the value to which the specified key is mapped, or -1 if this map contains no mapping
            for the key.
            """
            
            return self.hashmap[key]
            
    
        def remove(self, key: int) -> None:
            """
            Removes the mapping of the specified value key if this map contains a mapping for the key
            """
            
            self.hashmap[key] = -1