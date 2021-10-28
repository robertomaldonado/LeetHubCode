# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        vals = set()
        
        def dfs(node):
            if node:
                vals.add(node.val)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return len(vals) == 1