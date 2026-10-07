"""
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.
Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Return the sum of the two numbers as a linked list.

Example 1:
Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]
Explanation: 321 + 654 = 975.

Example 2:
Input: l1 = [9], l2 = [9]
Output: [8,1]

Constraints:
1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

"""
We create a dummy node so that building the answer linked list is easier, and current always points to the last node we created. 
We also keep carry, which stores the extra value when two digits add up to 10 or more. 
Inside the loop, val1 gets the current digit from l1 and val2 gets the current digit from l2. 
If one list has already ended, we simply use 0 for that list.

We calculate total = val1 + val2 + carry. total % 10 gives the digit that belongs in the current result node, 
while total // 10 gives the new carry. We create that result node, move current forward, and then move l1 and l2 forward when possible. 
The condition while l1 or l2 or carry is important because even after both lists finish, we may still need one final node for the carry.
"""

"""
Example : l1 = [1,2,3] represents the linked list 1 → 2 → 3, when the function starts, l1.val is 1, not 3
For l1 = [1,2,3] and l2 = [4,5,6], when the function starts, dummy is an empty ListNode(0), current points to dummy, and carry = 0. 
The first time we enter the while loop, l1.val = 1 so val1 = 1, and l2.val = 4 so val2 = 4. total = 1 + 4 + 0 = 5, 
so digit = 5 % 10 = 5 and carry = 5 // 10 = 0. We create ListNode(5) at current.next, move current to that new node, move l1 to node 2, 
and move l2 to node 5. On the second loop, val1 = 2 and val2 = 5, so total = 2 + 5 + 0 = 7, digit = 7, and carry = 0. 
We create node 7, so the result is now 5 → 7, then move l1 to 3 and l2 to 6. On the third loop, val1 = 3 and val2 = 6, so total = 3 + 6 + 0 = 9, 
digit = 9, and carry = 0. We create node 9, giving 5 → 7 → 9. Both l1 and l2 now become None and carry is 0, so the loop stops. 
Finally, we return dummy.next, which points to 5 → 7 → 9.
"""

"""
Time Complexity: O(max(n, m))
We process each node from both linked lists at most once.

Space Complexity: O(max(n, m))
The returned linked list contains approximately as many nodes as the longer input list, possibly one extra for the final carry. 
Excluding the output list itself, the extra working space is O(1).
"""

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def print_linked_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)

def main():
    l1 = build_linked_list([1, 2, 3])
    l2 = build_linked_list([4, 5, 6])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print_linked_list(result)


if __name__ == "__main__":
    main()