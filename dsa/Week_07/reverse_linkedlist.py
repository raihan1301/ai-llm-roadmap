"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
head = [0,1,2,3], that list is only a human-friendly representation. Your reverseList() function does not actually receive a Python list. 
NeetCode first converts those values into ListNode objects behind the scenes. Conceptually, 
it does something like node0 = ListNode(0), node1 = ListNode(1), node2 = ListNode(2), node3 = ListNode(3). 
When ListNode(0) is created, val = 0 and next = None at first. Then 
NeetCode connects the nodes by doing node0.next = node1, node1.next = node2, and node2.next = node3. node3.next stays None because 
it is the last node. So the real structure passed into your function is 0 -> 1 -> 2 -> 3 -> None, and head points to the node containing 0.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        """
        previous = None
        current  = node 0
        0 -> 1 -> 2 -> 3 -> None
        """

        while current:
            next_node = current.next
            """
            previous = None
            current = 0
            next_node = 1
            """
            current.next = previous
            """
            That changes 0.next from pointing to 1 to pointing to None: 0 -> None
            We did not lose node 1, because we saved it in next_node. Then:
            """

            previous = current
            current = next_node
            """
            so previous now points to node 0.
            so current now points to node 1.
            """

            """
            After 1st loop
            previous = 0
            current = 1
            0 -> None
            1 -> 2 -> 3 -> None

            2nd loop
            1 -> 0 -> None
            2 -> 3 -> None
            """
        return previous


def main():
    solution = Solution()

    input1 = [0,1,2,3]

    """
    below we are calling to build the linked list function
    """
    head = build_linked_list(input1)

    print("Original:")
    print_linked_list(head)

    result = solution.reverseList(head)
    print("Reversed:")
    print_linked_list(result)


"""
now if we are not using neetcode, we have to create node first from the input we have given in main above [0,1,2,3]
below is the code for that
"""

def build_linked_list(nums):
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head

    for num in nums[1:]:
        new_node = ListNode(num)
        current.next = new_node
        current = new_node

    return head

def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")
        current = current.next
    print("\n")


main() 

"""
Here is what happens when we build the list. First, head = ListNode(nums[0]) calls ListNode(0), 
so we create a node where val = 0 and next = None. Then current = head, so both head and current point to that node. 
The loop starts from [1,2,3]. For 1, we create new_node = ListNode(1), then current.next = new_node, 
which changes node 0 from 0 -> None into 0 -> 1 -> None. Then current = new_node, so current moves to node 1. 
The same happens for 2 and 3, producing 0 -> 1 -> 2 -> 3 -> None. After that, we pass head into reverseList(), 
which reverses those existing .next connections.
"""

"""
Time Complexity: O(n) — we visit every node exactly once.
Space Complexity: O(1) — we only use three pointer variables regardless of the size of the linked list.
"""