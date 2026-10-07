"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
input: root = [2,1,3], k = 1
Output: 1

Example 2:
Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:
1 <= k <= The number of nodes in the tree <= 10,000.
0 <= Node.val <= 10,000
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            current = current.right
"""
We use inorder traversal because for a Binary Search Tree, visiting nodes in the order left → current node → right gives the values 
from smallest to largest. We create an empty stack and set current = root. The inner while current: loop keeps moving as far left as possible 
while saving each node in the stack. When current becomes None, we have reached the smallest available node, so we pop it from the stack.

Every time we pop a node, we have found the next smallest value in the BST, so we decrease k by 1. 
When k == 0, that node is the kth smallest, so we return current.val. If we have not reached k yet, 
we move to current.right because the next larger value may be in that node's right subtree. Then the process repeats.
"""
"""
Example : 
We start with current = 4. We push 4, then move left to 3; push 3, then move left to 2; push 2, 
then current becomes None. The stack is now [4, 3, 2]. We pop 2, so k becomes 3. Then we pop 3, so k = 2. Then we pop 4, so k = 1. 
After processing 4, we move to its right child 5. We push and then pop 5, making k = 0, so we return 5.
"""
"""
Time Complexity: O(h + k)
We first travel down the tree height h, then process nodes until we reach the kth smallest. In the worst case, this becomes O(n).

Space Complexity: O(h)
The stack stores nodes along the tree height. For a balanced tree this is O(log n); for a completely skewed tree it can become O(n).
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
    root = [4,3,5,2,None] 
    k = 4

    root_tree = build_tree(root)

    solution = Solution()
    k_smallest = solution.kthSmallest(root_tree, k)

    print("Smallest in BST :", k_smallest)


if __name__ == "__main__":
    main()
