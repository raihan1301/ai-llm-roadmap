"""
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:
1 <= The number of nodes in the tree <= 30000.
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left_gain = max(dfs(node.left), 0) 
            right_gain = max(dfs(node.right), 0)

            current_path = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path)

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return max_sum   

"""
We create max_sum to store the best path sum found anywhere in the tree. It starts at float("-inf") because node values can all be negative. 
The dfs() function recursively calculates how much value each node can contribute upward to its parent. 
We first calculate left_gain and right_gain. If either subtree gives a negative result, 
we replace it with 0 because adding a negative path would only make our total smaller.

At every node, current_path = node.val + left_gain + right_gain represents the best path that passes through that node, 
possibly using both its left and right sides. We compare that against max_sum. However, when returning to the parent, 
we cannot return both sides because that would create a branching path. So we return node.val + max(left_gain, right_gain), 
meaning the parent can continue through only the better side.
"""

"""
For root = [1,2,3], node 2 has no children, so it returns 2; node 3 returns 3. 
At node 1, left_gain = 2 and right_gain = 3, so current_path = 1 + 2 + 3 = 6, and max_sum becomes 6. 
But node 1 would return only 1 + max(2,3) = 4 upward because a path continuing to a parent could only use one side. 
Since 1 is the root, the final answer remains 6.

The DFS starts at -15, goes left to 10, which returns 10. Then it goes right to 20; inside 20, node 15 returns 15. 
On the right side, node 5 first visits -5. Since -5 is negative, max(dfs(-5), 0) becomes 0, so node 5 returns 5. 
Now at node 20, left_gain = 15 and right_gain = 5, so current_path = 20 + 15 + 5 = 40, making max_sum = 40. 
Node 20 returns only 20 + max(15, 5) = 35 upward. Finally at -15, the path through the root is -15 + 10 + 35 = 30, which is smaller than 40, 
so the final answer remains 40.
"""

"""
Time Complexity: O(n)
We visit every node exactly once.

Space Complexity: O(h)
The recursive call stack depends on the height of the tree. For a balanced tree it is O(log n), and in the worst skewed case it becomes O(n).
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
    root = [-15,10,20,None,None,15,5,-5]

    root_tree = build_tree(root)

    solution = Solution()
    max_path_sum = solution.maxPathSum(root_tree)

    print("Maximum sum Path :", max_path_sum)


if __name__ == "__main__":
    main()

