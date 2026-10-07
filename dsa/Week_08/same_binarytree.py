"""
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:
0 <= The number of nodes in both trees <= 100.
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False
        """
        solution = Solution(), so Now solution is an object of the Solution class.
        solution.isSameTree(p, q) --> Python internally passes that object as self.
        self refers to solution. Then call the same isSameTree() method again on this same Solution object.
        This is recurssion
        In short : "Use my same tree-comparison function again, but now compare the left children."
        """
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        if left_same and right_same:
            return True
        else:
            return False

"""
IMP Note : 
Inside a class method, you generally use: self.isSameTree(...) because isSameTree belongs to the Solution object.
You cannot usually just write: isSameTree(p.left, q.left). because Python will look for a normal local/global function named isSameTree, 
    not the method attached to the current object.
self tells Python: call the isSameTree method that belongs to this Solution object.
If isSameTree were written outside the class as a normal function, then you could call it : than we can call isSameTree(p.left, q.left)
"""

"""
We compare the two trees node by node. If both current nodes are None, that part of both trees matches, so we return True. 
If only one is None, their structures are different, so we return False. 
If both nodes exist but their values are different, we also return False. 
Otherwise, we recursively compare the left children of both trees and the right children of both trees. 
The trees are only the same if both the left side and right side match all the way down.
"""
"""
Time Complexity: O(n) — in the matching case, we may visit every node once.
Space Complexity: O(h) — recursion uses stack space based on tree height.
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
    p = [1,2,3]
    q = [1,2,3]

    tree_1 = build_tree(p)
    tree_2 = build_tree(q)

    solution = Solution()
    same = solution.isSameTree(tree_1, tree_2)

    print("Is both tree same:", same)


if __name__ == "__main__":
    main()