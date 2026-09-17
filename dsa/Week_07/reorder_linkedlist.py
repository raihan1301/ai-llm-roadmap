"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as: [0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order: [0, 6, 1, 5, 2, 4, 3]

In the general case, label the nodes by their original zero-based positions from 0 to n - 1. 
After reordering, those original positions appear in this order: [0, n-1, 1, n-2, 2, n-3, ...]

These numbers represent node positions, not the values stored in the nodes.
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):

        if not head or not head.next:
            return

        slow = head
        fast = head
        """
        idea behind this is to finc the middle
        """

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            """
            Because fast moves 2 nodes for every 1 node that slow moves. So by the time fast reaches the end of the linked list, 
            slow has only travelled half the distance — which puts it at the middle.
            2 → 4 → 6 → 8 → 10
                    ↑
                    slow
            """

        """
        now we reverse the second half because than we can point to first node and add it
        """
        second = slow.next
        slow.next = None
        """
        so right now slow.val is 6, slow.next.val is 8, hence slow.next = 8->10
        also we do slow.next = None, so the connection is cut for slow cycle after middle
        """

        previous = None

        while second:
            """
            we are reversing the linkedlist as we did in reverse.linkedlist.py
            """
            next_node = second.next
            second.next = previous
            previous = second
            second = next_node

            """
            example where second = second : 8 → 10 → 11 → 12 → None
            previous :8 → None , second :10 → 11 → 12 → None
            previous : 10 → 8 → None, second : 11 → 12 → None
            """

        """
        merge both list
        """
        first = head
        second = previous

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        return head

def main():
    solution = Solution()

    input1 = [2, 4, 6, 8, 10]

    """
    below we are calling to build the linked list function
    """
    head = build_linked_list(input1)

    print("Original:")
    print_linked_list(head)

    result = solution.reorderList(head)
    print("Reorded:")
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
We first use slow and fast pointers to find the middle of the linked list. 
Then we take the second half and reverse its .next pointers so that what used to be the end of the list becomes the beginning of the second half.
Finally, we use first and second pointers and alternate their nodes: first node from the first half, first node from the reversed second half, 
then next from the first half, then next from the second half, until the second half is exhausted.
"""

"""
Time Complexity: O(n) — we traverse the list to find the middle, reverse half of it, and merge it.
Space Complexity: O(1) — we only use pointer variables and do not create another list.
"""