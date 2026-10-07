"""
Given a binary search tree (BST) where all node values are unique, 
and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. 
The ancestor is allowed to be a descendant of itself.

Example 1:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2: 
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:
2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.
"""

"""
Important wording it is BST
Because this is not just any binary tree — it is specifically a Binary Search Tree (BST), and the defining rule of a BST is: 
    for every node, all values in its left subtree are smaller than the node's value, and all values in its right subtree are larger
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right

            else:
                return current      

"""
We use the special property of a Binary Search Tree: every value smaller than the current node is on the left, and every larger value is on the right. 
We start with current = root. If both p and q are smaller than current, then their common ancestor must be somewhere on the left, 
so we move current = current.left. If both are larger, we move right. 
Otherwise, they have split to different sides, or one of them is equal to current, which means the current node is the lowest common ancestor, 
so we return it.
"""
"""
For root = [5,3,8,1,4,7,9,null,2], p = 3, and q = 8,
we start at current = 5. 3 < 5 but 8 > 5, so they are on different sides of node 5; therefore 5 is the LCA. 
For p = 3 and q = 4, we start at 5; both are smaller, so we move left to 3. 
Now p.val == current.val, so they no longer both belong strictly to one side, meaning node 3 is the LCA. 
This also shows why a node is allowed to be its own ancestor.
"""
"""
Time Complexity: O(h) — we move down one level at a time, where h is the tree height. 
    In a balanced BST this is about O(log n), while in a skewed BST it can be O(n).

Space Complexity: O(1) — we only use the current pointer.
"""

def insert_bst(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)

    return root


def find_node(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    current = root

    while current:
        if value == current.val:
            return current

        if value < current.val:
            current = current.left
        else:
            current = current.right

    return None

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
    values =[5,3,8,1,4,7,9,None,2] 

    root = build_tree(values)

    p = find_node(root, 3)
    q = find_node(root, 8)

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)

    print("LCA of given number in BST :", lca.val)


if __name__ == "__main__":
    main()
