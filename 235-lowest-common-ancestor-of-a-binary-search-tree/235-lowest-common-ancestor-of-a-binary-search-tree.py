# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
            (2)
        /          \ 
      (3)          (0)
    /    \       /     \ 
   (8)  (9)    (1)    (7)
Input: Tree ^, p=1, q=3
Output: 2

++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Recurse to ref of tree
2. Verify which subtree I have
3. Return left, right or current node
++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def _lowest_ancestor(node):
            if not node: return None
            if node == p or node == q:
                return node
            
            left = _lowest_ancestor(node.left)
            right = _lowest_ancestor(node.right)
            
            if not left:
                return right
            elif not right:
                return left
            else:
                return node
                
        if not root: return None    
        return _lowest_ancestor(root)
        
        
        
        