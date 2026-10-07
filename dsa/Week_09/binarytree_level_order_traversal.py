"""
Given a binary tree root, return the level order traversal of it as a nested list, 
where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 2000.
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        result = []

        queue = deque([root])
        """
        We can do it without deque; deque is just the cleanest and most efficient queue structure in Python for BFS. 
        A normal list can also work, but if you use pop(0), removing from the front is O(n) because Python has to shift the remaining elements.
        deque.popleft() is O(1), which is why it is preferred for level-order traversal. So deque is not required, 
        but it is the standard choice for tree BFS.
        """ 

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()

                level.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            result.append(level)

        return result
"""
We use a deque as a queue and start by adding the root. Each while loop processes exactly one tree level. 
level_size = len(queue) tells us how many nodes belong to the current level before we start adding the next level's children. 
We remove each node from the front with popleft(), add its value to level, and add its left and right children to the queue. 
After all nodes from that level are processed, we append the completed level list to result. This continues until the queue is empty.
"""   
"""
Time Complexity: O(n) — every node is visited once.
Space Complexity: O(n) — the queue can hold many nodes from one tree level, and result stores all node values.
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
    input_1 =[1,2,3,4,5,6,7]

    tree_1 = build_tree(input_1)

    solution = Solution()
    traversal = solution.levelOrder(tree_1)

    print("Binary Tree level order Traversal:", traversal)


if __name__ == "__main__":
    main()