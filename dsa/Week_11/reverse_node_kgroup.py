"""
You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. 
If there are fewer than k nodes left, leave the nodes as they are.
Return the modified list after reversing the nodes in each group of k.
You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:
Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The length of the linked list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 100
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getkth(group_prev, k)

            if not kth:
                break

            group_next = kth.next

            previous = group_next
            current = group_prev.next

            while current != group_next:
                next_node = current.next

                current.next = previous

                previous = current
                current = next_node

            old_group_start = group_prev.next

            group_prev.next = kth
            group_prev = old_group_start

        return dummy.next

    def getkth(self, current: ListNode, k: int) -> Optional[ListNode]:
        while current and k > 0:
            current = current.next
            k -= 1

        return current

"""
We first create a dummy node pointing to head, and group_prev points to that dummy node. 
group_prev always represents the node immediately before the group we are about to reverse. 
Inside the main loop, getKth(group_prev, k) moves forward k nodes to check whether a complete group exists. 
If it returns None, there are fewer than k nodes remaining, so we stop. 
Otherwise, group_next = kth.next remembers the first node after the current group because we need to reconnect the reversed group to it later.

To reverse the group, previous starts at group_next and current starts at the first node of the group. While current != group_next, 
we save current.next in next_node, reverse current.next so it points to previous, 
then move previous and current forward. After the group is reversed, old_group_start stores the node that used to be first 
but is now the last node of the reversed group. We connect group_prev.next to kth, which is now the first node of the reversed group, 
then move group_prev to old_group_start so the next group can be processed.
"""

"""
For head = [1,2,3,4,5,6] and k = 3, 
dummy points to 1 and group_prev = dummy. getKth(group_prev, 3) moves from dummy → 1 → 2 → 3, so kth = 3, and group_next = 4. 
We set previous = 4 and current = 1. First loop: next_node = 2, then 1.next = 4, previous = 1, and current = 2. 
Second loop: next_node = 3, then 2.next = 1, previous = 2, and current = 3. 
Third loop: next_node = 4, then 3.next = 2, previous = 3, and current = 4, so the loop stops because current == group_next. 
old_group_start was node 1, so we connect dummy.next = 3, giving 3 → 2 → 1 → 4 → 5 → 6, and move group_prev to node 1. 
Now getKth(1, 3) reaches node 6, so the same process reverses 4 → 5 → 6 into 6 → 5 → 4. 
The final list becomes 3 → 2 → 1 → 6 → 5 → 4.
"""

"""
Time Complexity: O(n)
Each node is visited a constant number of times while finding group boundaries and reversing the groups.

Space Complexity: O(1)
We only use a few pointer variables and modify the existing linked-list pointers in place.
"""

class Solution_v2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        groupPrev = dummy = ListNode(0, head)
        while True:
            # walk k steps to find the group's last node; if we fall off, we're done
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            groupNext = kth.next          # first node of the *next* group (exclusive boundary)

            # reverse [groupPrev.next .. kth]
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnect
            newTail = groupPrev.next       # old head is now the tail
            groupPrev.next = kth           # kth is the new head of this group
            groupPrev = newTail            # tail becomes prev for the next group

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
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    k = 3

    solution = Solution()
    result = solution.reverseKGroup(head, k)

    print_linked_list(result)


if __name__ == "__main__":
    main()