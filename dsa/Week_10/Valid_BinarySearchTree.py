"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:
1 <= The number of nodes in the tree <= 10000.
-1000000000 <= Node.val <= 1000000000
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, minimum, maximum):
            if node is None:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            left_valid = validate(node.left, minimum, node.val)
            right_valid = validate(node.right, node.val, maximum)

            return left_valid and right_valid

        return validate(root, float("-inf"), float("inf")) 
    """
    float("-inf") means negative infinity in Python
    It is a special floating-point value that is smaller than every normal number. 
    For example, -1000 > float("-inf") and even -10**100 > float("-inf") are both True.
    """

"""
We create a helper function validate() that checks whether each node falls inside an allowed range. 
The root initially has no real restriction, so we give it a range from negative infinity to positive infinity. 
When we go left, the current node's value becomes the new maximum, because every node in that left subtree must be smaller than the current node. 
When we go right, the current value becomes the new minimum, because every node in that right subtree must be larger. 
If any node falls outside its allowed range, we return False. Otherwise we recursively validate both sides, and both must return True.
"""
"""
Example:
For example, with [5,3,8,1,4,7,9], node 5 starts with (-inf, inf). 
When we go left to 3, its allowed range becomes (-inf, 5). When we then go right from 3 to 4, its range becomes (3, 5), so 4 is valid. 
On the right of 5, node 8 gets the range (5, inf), and node 7 underneath it gets (5, 8). 
This is important because we are not only comparing a node with its direct parent; we are checking that it obeys all ancestor limits.
"""
"""
Time Complexity: O(n) — every node is checked once.
Space Complexity: O(h) — recursion uses stack space based on tree height.
"""

def build_tree(nums):

    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])

    index = 1

    while queue and index < len(nums):
        current = queue.popleft()

        if index < len(nums) and nums[index] is not None:
            current.left = TreeNode(nums[index])
            queue.append(current.left)

        index += 1

        if index < len(nums) and nums[index] is not None:
            current.right = TreeNode(nums[index])
            queue.append(current.right)

        index += 1

    return root

def main():
    root = [5,3,8,1,4,7,9]

    root_tree = build_tree(root)

    solution = Solution()
    valid_bst = solution.isValidBST(root_tree)

    print("Is this Valid BST :", valid_bst)


if __name__ == "__main__":
    main()