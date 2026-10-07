"""
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.


Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2: 
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True

        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

"""
We use two recursive functions. isSubtree() moves through every node of the main root tree and asks, 
"If I start here, is this entire tree exactly the same as subRoot?" That exact comparison is handled by isSameTree().
If isSameTree(root, subRoot) returns True, we immediately found the subtree. 
If not, we recursively try again starting from root.left and then root.right. or is used because we only need to find a match on either side.

Inside isSameTree(), if both nodes are None, that part matches. If only one is None, the structures are different. 
If their values differ, the trees are different. Otherwise, we recursively compare left with left and right with right, and both sides must match. 
So the main idea is: search every possible starting node in the big tree, and whenever you find a candidate, compare the entire structure from there.
"""
"""
Example: 
For root = [1,2,3,4,5] and subRoot = [2,4,5], 
we first compare root node 1 with subRoot node 2; their values are different, so isSameTree() returns False. 
Then isSubtree() moves to the left child, node 2, and compares that subtree with subRoot. Now 2 == 2, 
then its left nodes 4 == 4, its right nodes 5 == 5, and all corresponding children eventually reach None together, so isSameTree() returns True. 
Therefore isSubtree() returns True.
"""
"""
Time Complexity: O(n * m) in the worst case, where n is the number of nodes in root and m is the number of nodes in subRoot. 
    We may potentially compare subRoot against many nodes in the main tree.
Space Complexity: O(h) for recursion, depending on the heights of the trees.
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
    root =[1,2,3,4,5]  
    subRoot = [2,4,5]

    root_tree = build_tree(root)
    subRoot_tree = build_tree(subRoot)

    solution = Solution()
    SubTree = solution.isSubtree(root_tree, subRoot_tree)

    print("is Subroot is Subtree of Root Tree :", SubTree)


if __name__ == "__main__":
    main()
