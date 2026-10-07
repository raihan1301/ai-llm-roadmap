"""
You are given the root of a binary tree. 
Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,4,null,5]
Output: [1,3,5]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,2]
Output: [1,2]

Example 4:
Input: root = []
Output: []

Constraints:
0 <= number of nodes in the tree <= 100
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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:

        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current = queue.popleft()

                if i == level_size - 1:
                    result.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

        return result
"""
We start by returning an empty list if there is no root. Otherwise, we create result to store the visible nodes 
and a queue containing the root so we can do a BFS level by level. 
At the beginning of each level, level_size = len(queue) tells us exactly how many nodes belong to that level. 
We then remove those nodes one at a time using popleft(). Because the nodes are processed from left to right, 
the node where i == level_size - 1 is the last node in that level, which is the one visible from the right side, 
so we add its value to result. While processing each node, we also add its left and right children to the queue for the next level. 
When the queue becomes empty, every level has been processed and we return result.
"""

"""
Example : For root = [1,2,3,None,4,None,5], the first level has queue [1], so 1 is the last node and gets added to result = [1]. 
The next level contains [2,3]; we process 2 first and 3 second, so 3 is added and result = [1,3]. Their children add 4 and 5 to the next level, 
making the queue [4,5]. We process 4 then 5, and because 5 is the last node at that level, it is added, giving the final result [1,3,5].
"""

"""
Time Complexity: O(n) — every node is visited once.
Space Complexity: O(n) — the queue may hold many nodes from one level.
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
    input_1 =[1,2,3,None,4,None,5]

    tree_1 = build_tree(input_1)

    solution = Solution()
    rightside = solution.rightSideView(tree_1)

    print("Binary Tree Right Side View:", rightside)


if __name__ == "__main__":
    main()