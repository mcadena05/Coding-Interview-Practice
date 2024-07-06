# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkIsSameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1  or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            leftMatch = checkIsSameTree(root1.left, root2.right)
            
            if not leftMatch:
                return False
            
            rightMatch = checkIsSameTree(root1.right, root2.left)
            
            if not rightMatch:
                return False
            return True

        return checkIsSameTree(root.left, root.right) 

        
        