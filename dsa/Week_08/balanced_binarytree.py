"""
Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: true

Example 2:
Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):

            if node is None:
                return 0

            left_height = height(node.left)

            if left_height == -1:
                return -1

            right_height = height(node.right)

            if right_height == -1:
                return -1

            """
            abs() means absolute value — it removes the negative sign.
            How different are the left and right subtree heights?
            """ 
            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return height(root) != -1

"""
We create a helper function height() that calculates the height of each subtree. 
If a node is None, its height is 0. We get the left height and right height, 
then check abs(left_height - right_height). If the difference is greater than 1, that subtree is not balanced, 
so we return -1 as a special signal. 
That -1 keeps traveling upward through the recursive calls, so we do not need a separate boolean variable. 
If the subtree is balanced, we return its normal height using 1 + max(left_height, right_height). 
Finally, if the root returns anything other than -1, the whole tree is balanced.
"""
"""
Time Complexity: O(n) — every node is visited once.
Space Complexity: O(h) — recursion uses stack space based on the height of the tree.
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
    nums = [1,2,3,None,None,4]

    root = build_tree(nums)

    solution = Solution()
    balanced = solution.isBalanced(root)

    print("Tree is Balanced : ", balanced)


if __name__ == "__main__":
    main()