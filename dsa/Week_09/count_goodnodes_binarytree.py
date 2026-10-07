"""
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x 
contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:
Input: root = [2,1,1,3,null,1,5]
Output: 3

Example 2:
Input: root = [1,2,-1,3,4]
Output: 4

Constraints:
1 <= number of nodes in the tree <= 100,000
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
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if node is None:
                return 0

            good = 0

            if node.val >= max_value:
                good = 1

            max_value = max(max_value, node.val)

            left_good = dfs(node.left, max_value)
            right_good = dfs(node.right, max_value)

            return good + left_good + right_good

        return dfs(root, root.val)       

"""
We use DFS and carry one important value with us: max_value, which represents the largest node value seen on the path from the root to the current node.
At each node, we check whether node.val >= max_value; if yes, this node is good, so good = 1, otherwise it stays 0. 
Then we update max_value using max(max_value, node.val) before going deeper, because the children need to know the largest value seen so far. 
We recursively count good nodes in the left subtree and right subtree, then return good + left_good + right_good. 
The first call starts with root.val because the root is always good.
"""

"""
Example : For root = [2,1,1,3,None,1,5], 
we start at node 2 with max_value = 2, so 2 >= 2 and count becomes 1. 
Going left to node 1, the max is still 2, so 1 < 2 and it is not good. 
From there node 3 is checked against max 2, so 3 >= 2, making it good and updating the path maximum to 3. 
On the right side, node 1 is not good because max is 2, but node 5 later sees max 2, so 5 >= 2 and is good. Total good nodes = 3.
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
    input_1 =[2,1,1,3,None,1,5]

    tree_1 = build_tree(input_1)

    solution = Solution()
    good_node = solution.goodNodes(tree_1)

    print("Binary Tree has good nodes :", good_node)


if __name__ == "__main__":
    main()