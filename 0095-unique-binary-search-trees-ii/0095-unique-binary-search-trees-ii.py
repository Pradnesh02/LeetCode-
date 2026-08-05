# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
            
        memo = {}

        def build_trees(start, end):
            if start > end:
                return [None]
                
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            
            for root_val in range(start, end + 1):
                # Generate all left and right subtrees recursively
                left_trees = build_trees(start, root_val - 1)
                right_trees = build_trees(root_val + 1, end)
                
                # Combine each left and right subtree with the current root
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees

        return build_trees(1, n)