# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # The current node's value must strictly fit within (low, high)
            if not (low < node.val < high):
                return False
            
            # Recursively check left and right subtrees with updated bounds
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
            
        return validate(root)