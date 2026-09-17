"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        we have to ouput linked list not a normal list
        """
        dummy = ListNode()
        current = dummy

        node_1 = list1
        node_2 = list2

        while node_1 and node_2:
            if node_1.val <= node_2.val:
                current.next = node_1
                node_1 = node_1.next

            else:
                current.next = node_2
                node_2 = node_2.next

            current = current.next

        if node_1:
            current.next = node_1

        if node_2:
            current.next = node_2

        return dummy.next

def main():
    solution = Solution()

    input1 = [0,1,2,3]
    input2 = [1, 3, 5]

    """
    below we are calling to build the linked list function
    """
    head1 = build_linked_list(input1)
    head2 = build_linked_list(input2)

    print("Original:")
    print_linked_list(head1)
    print_linked_list(head2)

    result = solution.mergeTwoLists(head1, head2)
    print("Merged:")
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
We first take the normal Python lists [1,2,4] and [1,3,5] and use build_linked_list() to create actual ListNode objects connected through .next.
Then we pass those two linked-list heads into mergeTwoLists(). Inside the merge function, dummy gives us an easy starting point, 
current tracks the last node in the result, and node_1 and node_2 move through the two lists. 
We compare their .val values, connect the smaller node to current.next, move that list forward, and continue until one list ends. 
Then we attach the remaining nodes from the other list and return dummy.next, which is the real head of the merged linked list.
"""
"""
Time Complexity: O(n + m)
Space Complexity: O(1) for the merge itself, because it reuses the existing nodes.
"""