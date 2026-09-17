"""
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3: 
Input: root = []
Output: []

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
"""
We first check if root is None; if it is, there is nothing to invert, so we return None. 
Otherwise, we swap the current node's left and right children. 
Then we recursively call invertTree() on the new left subtree and the new right subtree so the same swap happens at every node in the tree. 
Once all nodes have been processed, we return the original root, which now points to the fully inverted tree.
"""

"""
below is the simple version of build tree, for complex none value see other tree problems
"""
def build_tree(nums):

    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])

    index = 1

    while queue and index < len(nums):
        current = queue.popleft()

        if index < len(nums):
            current.left = TreeNode(nums[index])
            queue.append(current.left)
            index += 1

        if index < len(nums):
            current.right = TreeNode(nums[index])
            queue.append(current.right)
            index += 1

    return root
"""
build_tree() first converts the normal Python list into actual TreeNode objects. 
Node 1 becomes the root, then 2 and 3 become its left and right children, then 4,5 are connected under 2, and 6,7 under 3. 
invertTree() starts at node 1, swaps its left and right children, then recursively performs the same swap at every child node. 
Finally, tree_to_list() lets us print the tree in the same level-order format used by NeetCode.
"""

def tree_to_list(root):

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result

def main():
    nums = [1,2,3,4,5,6,7]

    root = build_tree(nums)
    print("Original Tree:")
    print(tree_to_list(root))

    solution = Solution()
    inverted_root = solution.invertTree(root)
    print("Inverted Tree:")
    print(tree_to_list(inverted_root))


if __name__ == "__main__":
    main()

"""
Time Complexity: O(n) — every node is visited once.

Space Complexity: O(h) — recursion uses the call stack, where h is the height of the tree. 
In a balanced tree this is about O(log n), while in a completely skewed tree it can become O(n).
"""