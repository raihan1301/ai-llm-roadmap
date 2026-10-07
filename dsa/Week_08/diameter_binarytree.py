"""
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. 
The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. 
Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:
Input: root = [1,null,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:
Input: root = [1,2,3]
Output: 2

Constraints:
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        """
        We are creating a nested function inside the function to get the height length from each node
        """
        def height(node):
            """
            nonlocal is specifically used inside a nested function when you want to modify a variable that belongs to the surrounding function.
            """
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return self.diameter
"""
We first set self.diameter = 0 to remember the biggest diameter found so far. 
The height() function goes down to the bottom of the tree and returns the height of each subtree. 
At every node, we calculate left_height + right_height, because that represents the longest path passing through that node. 
If that path is bigger than the diameter we already found, we update self.diameter. 
The function still returns only the larger of the left or right height plus 1, because the parent can only continue through one branch.
"""

"""
This is about as simple as the efficient O(n) solution gets. 
The reason it feels slightly more complex than Maximum Depth is that you are calculating two things at once:
    returning the height upward
    storing the diameter globally

Time Complexity: O(n) : every node is visited once.
Space Complexity: O(h) : recursion uses stack space based on the tree height.
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
    nums = [1,None,2,3,4,5]

    root = build_tree(nums)

    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)

    print("Maximum diameter: ", diameter)


if __name__ == "__main__":
    main()