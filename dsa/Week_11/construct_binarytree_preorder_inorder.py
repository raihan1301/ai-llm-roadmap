"""
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:
1 <= inorder.length <= 2001.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        inorder_index = {}

        for i, value in enumerate(inorder):
            inorder_index[value] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)
            middle = inorder_index[root_value]

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root
        
        return build(0, len(inorder) - 1) 

"""
We first create inorder_index, a dictionary that stores where every value appears inside inorder. 
This lets us instantly find where the current root divides the tree into its left and right subtrees. 
We also keep preorder_index, which tells us which value from preorder should become the next root. 
Because preorder traversal follows root → left → right, the next unused preorder value is always the root of the current subtree.

The recursive build(left, right) function represents the section of inorder that belongs to the current subtree. 
If left > right, there are no nodes, so we return None. Otherwise, we take the next preorder value as the root, 
find its position middle inside inorder, then recursively build everything to the left of middle as root.left and everything to the right as root.right.
Finally, we return the completed root.
"""

"""
For preorder = [1,2,3,4] and inorder = [2,1,3,4], 
preorder_index = 0, so the first root is 1. In inorder, 1 is at index 1, so [2] belongs to the left subtree and [3,4] belongs to the right subtree. 
The next preorder value is 2, which becomes the left child. Then preorder_index reaches 2, so 3 becomes the root of the right subtree. 
In inorder, 3 has nothing on its left and 4 on its right, so 4 becomes the right child of 3. 
The final tree is 1 with left child 2, right child 3, and 3 has right child 4.
"""

"""
Time Complexity: O(n)
We visit each node once, and the dictionary lets us find each root's inorder position in O(1).

Space Complexity: O(n)
The dictionary stores all n values, and recursion can also use up to O(n) space in the worst case.
"""

def print_tree(root):
    if not root:
        print([])
        return

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print(result)



def main():
    preorder = [1,2,3,4]
    inorder = [2,1,3,4]

    solution = Solution()
    binary_tree = solution.buildTree(preorder, inorder)

    print_tree(binary_tree)


if __name__ == "__main__":
    main()
