"""
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, 
which may point to any node in the list, or null.

Create a deep copy of the list. The deep copy should consist of exactly n new nodes, each including:
The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node

Note: None of the pointers in the new list should point to nodes in the original list.
Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, 
or null if it does not point to any node.

Example 1:
Input: head = [[3,null],[7,3],[4,0],[5,1]]
Output: [[3,null],[7,3],[4,0],[5,1]]

Example 2:
Input: head = [[1,null],[2,2],[3,2]]
Output: [[1,null],[2,2],[3,2]]

Constraints:
0 <= n <= 100
-100 <= Node.val <= 100
Node values are not guaranteed to be unique.
random is null or is pointing to some node in the linked list.
"""

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        old_to_new = {}

        current = head

        # first create copy of every node
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head

        #second connect next and random pointers
        while current:
            copied_node = old_to_new[current]

            copied_node.next = old_to_new.get(current.next)
            copied_node.random = old_to_new.get(current.random)

            current = current.next

        return old_to_new[head]

"""
We first create a dictionary called old_to_new. The key is an original node object, and the value is its new copied node. 
In the first loop, we walk through the original list and create a brand-new Node for every original node, but we do not connect anything yet. 
In the second loop, we take each original node, find its copied version from the dictionary, 
and set the copied node's next and random pointers by looking up the copied versions of current.next and current.random. 
Using .get() is useful because if either pointer is None, the dictionary returns None. 
Finally, old_to_new[head] gives us the copied version of the original head.
"""
"""
For [[3,None],[7,3],[4,0],[5,1]], suppose the original nodes are A=3, B=7, C=4, D=5. 
The first loop creates new nodes A'=3, B'=7, C'=4, D'=5, so the dictionary stores A→A', B→B', C→C', D→D'. 
Then if original B.random = D, we set B'.random = old_to_new[D], which gives D'. 
If original C.random = A, then C'.random = A'. 
So the copied list has the same shape and values, but every pointer stays entirely inside the copied list.
"""
"""
Time Complexity: O(n) — we go through the list twice.
Space Complexity: O(n) — the dictionary stores one mapping for every node.
"""

def build_random_list(data):
    if not data:
        return None

    nodes = []

    for value, random_index in data:
        nodes.append(Node(value))

    # Connect next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Connect random pointers
    for i, (_, random_index) in enumerate(data):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


def print_random_list(head):
    nodes = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    result = []

    for node in nodes:
        random_index = None

        if node.random is not None:
            random_index = nodes.index(node.random)

        result.append([node.val, random_index])

    print(result)


def main():
    data = [
        [3, None],
        [7, 3],
        [4, 0],
        [5, 1]
    ]

    head = build_random_list(data)

    print("Original:")
    print_random_list(head)

    solution = Solution()
    copied_head = solution.copyRandomList(head)

    print("Copied:")
    print_random_list(copied_head)

    print("Same first node object?", head is copied_head)


if __name__ == "__main__":
    main()