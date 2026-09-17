"""
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists. 
The tail node of the list will set it's next pointer to the index-th node. 
If index = -1, then the tail node points to null and no cycle exists.
Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1
Output: false

Constraints:
0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head
        """
        we create two pointers and both will start at 1st node
        """

        while fast and fast.next:
            """
            meaning fast is not none and fast.next pointer is also not none
            """
            slow = slow.next
            fast = fast.next.next

            """
            we will check the slow to just one pointer ahead and fast will be 2 steps at a time
            so if there is a cycle it will eventually catch the small again in the loop
            """

            if slow == fast:
                return True

        return False

def main():
    solution = Solution()

    input1 = [0,1,2,3]
    index = 1

    """
    below we are calling to build the linked list function
    """
    head = build_linked_list(input1, index)

    print("Original:")
    print_linked_list(head)

    result = solution.hasCycle(head)
    print("Cycle Detection:")
    print_linked_list(result)


"""
now if we are not using neetcode, we have to create node first from the input we have given in main above [0,1,2,3]
below is the code for that
"""

def build_linked_list(nums, index):
    if not nums:
        return None

    nodes = []

    head = ListNode(nums[0])
    current = head

    for num in nums:
        nodes.append(ListNode(num))

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]

    if index != -1:
        nodes[-1].next = nodes[index]

    return nodes[0]

def print_linked_list(head):
    current = head

    while current:
        print(current.val, end="")
        current = current.next
    print("\n")


main()

"""
For nums = [1,2,3,4], we first create four separate ListNode objects and store them in nodes. 
Then we connect them normally as 1 -> 2 -> 3 -> 4. Because index = 1, we change the last node's .next so that node 4 points back to nodes[1], 
which is the node containing 2. The real structure therefore becomes 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4.... 
We then pass the first node into hasCycle(), where slow moves one node at a time and fast moves two nodes at a time. 
Since there is a loop, they eventually meet and the function returns True.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1) for hasCycle() itself. The standalone build_linked_list() uses O(n) extra space 
    because we store the nodes in a Python list so we can easily connect the last node back to a specific index.
"""