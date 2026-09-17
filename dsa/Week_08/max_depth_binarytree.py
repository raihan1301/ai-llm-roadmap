"""
Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0

Constraints:
0 <= The number of nodes in the tree <= 100.
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
"""
We first check whether the current root is None; if it is, that branch has depth 0. 
Otherwise, we recursively find the depth of the left subtree and the right subtree. 
We take whichever side is deeper using max(left_depth, right_depth), then add 1 for the current node. 
This repeats until every branch reaches None, and the final result is the number of nodes along the longest root-to-leaf path.
"""

"""
Time Complexity: O(n) — every node is visited once.

Space Complexity: O(h) — recursion uses the call stack based on tree height. 
In a balanced tree this is O(log n), while a completely one-sided tree can be O(n).
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

"""
above build tree is used for complex trees
"""
"""
We first use build_tree() to convert the normal Python list [1,2,3,None,None,4] into actual TreeNode objects connected through .left and .right. 
Then maxDepth() recursively checks the depth of the left subtree and the right subtree for every node. 
If a node is None, that branch contributes depth 0. For a real node, we take the larger of the left and right depths and add 1 for the current node. 
For this example, node 4 has depth 1, node 3 has depth 2, and the root node 1 has depth 3, so the final result is 3.
"""

def main():
    nums = [1, 2, 3, None, None, 4]

    root = build_tree(nums)

    solution = Solution()
    depth = solution.maxDepth(root)

    print("Maximum Depth:", depth)


if __name__ == "__main__":
    main()

"""
IMP:
It knows the depth because each recursive call returns a number, and those returned numbers build back up as the recursion finishes.

At node 4 :
left_depth = self.maxDepth(None)   # 0
right_depth = self.maxDepth(None)  # 0
return 1 + max(0, 0)

At node 3: 
left_depth = 1   # from node 4
right_depth = 0
return 1 + max(1, 0)
.
.
.
At node 1:
left_depth = 1
right_depth = 2
"""