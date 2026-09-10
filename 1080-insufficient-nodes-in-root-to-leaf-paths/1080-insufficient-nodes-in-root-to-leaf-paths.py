# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Base case: Leaf node
        if not root.left and not root.right:
            return root if root.val >= limit else None

        # Recursively update left and right subtrees
        remaining_limit = limit - root.val
        root.left = self.sufficientSubset(root.left, remaining_limit)
        root.right = self.sufficientSubset(root.right, remaining_limit)

        # If both children are None after pruning, this node becomes a dead end
        if not root.left and not root.right:
            return None

        return root