# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal total_tilt
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Accumulate the tilt for the current node
            total_tilt += abs(left_sum - right_sum)

            # Return the sum of values of the subtree rooted at this node
            return left_sum + right_sum + node.val

        dfs(root)
        return total_tilt