# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_depth(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)

        if left_depth == right_depth:
            # Left subtree is a perfect binary tree of height left_depth
            # (1 << left_depth) accounts for the 2^left_depth - 1 nodes in the left subtree + 1 for root
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree of height right_depth
            return (1 << right_depth) + self.countNodes(root.left)