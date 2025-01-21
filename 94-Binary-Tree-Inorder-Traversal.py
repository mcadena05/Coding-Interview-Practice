# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

from typing import Optional


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        output = []
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            output.append(current.val)
            current = current.right
        return output


        # output = []

        # def in_order(root):
        #     if not root:
        #         return
        #     in_order(root.left)
        #     output.append(root.val)
        #     in_order(root.right)
        # in_order(root)
        # return output