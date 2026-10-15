"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
    Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
Output:
[null, null, 10, null, null, 20, -1]
Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        previous = node.prev
        next_node = node.next

        previous.next = next_node
        next_node.prev = previous

    def insert(self, node):
        previous = self.right.prev

        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
"""
Code Explanation:
We need two data structures because the problem requires both get() and put() to be O(1). 
self.cache is a dictionary where each key points directly to its Node, so finding a key is O(1). 
Then we use a doubly linked list to track usage order. left and right are dummy nodes: 
the node closest to left is the least recently used, and the node closest to right is the most recently used. 
remove() disconnects a node from its current position, while insert() always places a node immediately before right, making it the most recently used.

When get(key) is called, if the key does not exist we return -1. If it exists, we get its node directly from the dictionary, 
remove it from its current position, insert it at the right side because it was just used, and return its value. 
For put(), if the key already exists, we remove its old node first. Then we create the updated node, store it in the dictionary, 
and insert it at the most-recently-used side. If the cache now exceeds capacity, self.left.next is the least recently used node, 
so we remove it from both the linked list and dictionary.
"""
"""
Example:
For capacity = 2, when LRUCache(2) starts, cache = {} and the linked list is left ↔ right. 
put(1,10) creates node 1, stores cache[1] = node1, and inserts it before right, so the order is left ↔ 1 ↔ right. 
get(1) finds node 1, removes it and inserts it back at the most-recent position, then returns 10. 
put(2,20) creates node 2, so the order becomes left ↔ 1 ↔ 2 ↔ right; this means 1 is least recently used and 2 is most recently used. 
Then put(3,30) inserts 3, giving left ↔ 1 ↔ 2 ↔ 3 ↔ right. Now the cache size is 3, which exceeds capacity 2, 
so lru = self.left.next gives node 1; we remove node 1 and delete cache[1], leaving left ↔ 2 ↔ 3 ↔ right. 

Then get(2) finds node 2, removes it from its current position and inserts it beside right, so the order becomes left ↔ 3 ↔ 2 ↔ right, and it returns 20
Finally, get(1) does not find key 1 in the dictionary, so it returns -1.
"""
"""
Time Complexity: O(1) average for both get() and put().
Dictionary lookup, insertion, and deletion are O(1) average, and moving a known linked-list node is also O(1).

Space Complexity: O(capacity)
The dictionary and linked list store at most capacity cache entries.
"""

def main():
    lru = LRUCache(2)

    lru.put(1, 10)
    print("get(1):", lru.get(1))

    lru.put(2, 20)

    lru.put(3, 30)

    print("get(2):", lru.get(2))
    print("get(1):", lru.get(1))


if __name__ == "__main__":
    main()