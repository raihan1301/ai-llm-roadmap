"""
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        we will take example : [1,2,3,4,5,6] n=1
        """
        dummy = ListNode(0,head)
        """
        so dummy becomes : dummy → 1 → 2 → 3 → 4 → 5 → 6 → None
        """

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            """
            so now we move with the range 1+1 = 2
            """
            fast = fast.next
            """
            now after for loop fast will be
            fast → 1
            fast → 2
            """

        while fast:
            """
            so this will run till fast is none
            right now fast is 2 → 3 → 4 → 5 → 6 → None
            """

            slow = slow.next
            fast = fast.next
            """
            so just 2 loops example
            slow = 1, fast = 3
            slow = 2, fast = 4
            slow = 3, fast = 5
            slow = 4, fast = 6
            slow = 5, fast = none and it will stop the while loop
            """

        slow.next = slow.next.next
        """
        this will remove the nth node because we are replace slow.next which is 6 to slow.next.next which is none
        if there was any other digit it will be replace by that

        now slow is just a pointer so actually we removed it from the dummy list and thats why no 
        dummy is dummy → 1 → 2 → 3 → 4 → 5 → None
        """
        return dummy.next

def main():
    solution = Solution()

    input1 = [1,2,3,4,5,6]
    index = 1

    """
    below we are calling to build the linked list function
    """
    head = build_linked_list(input1)

    print("Original:")
    print_linked_list(head)

    result = solution.removeNthFromEnd(head, index)
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
We create a dummy node before head so removing the first real node is easy. Then slow and fast both start at dummy. 
We move fast ahead by n + 1 positions so there is always a gap of n nodes between slow and fast. After that, 
we move both pointers one step at a time until fast reaches None. At that moment, slow is sitting one node before the node we need to remove, 
so slow.next = slow.next.next skips that node. Finally, we return dummy.next, which points to the correct head of the updated linked list.
"""

"""
Time Complexity: O(n) — we traverse the linked list at most twice with the pointers.
Space Complexity: O(1) — only a few pointer variables are used.
"""