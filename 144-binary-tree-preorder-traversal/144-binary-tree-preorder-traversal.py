# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Pre order traversal.
  Recursive approach. Uses a stack, the call stack
            4
    /             \
   3               2
  / \             /
 1   5           8
 
 [4,3,1,5,2,8]
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      
        def traverse(root, ans):
          if not root: return
          ans.append(root.val)
          if root.left: 
            traverse(root.left, ans)
          if root.right:
            traverse(root.right, ans)
        
        ans = []
        traverse(root, ans)
        return ans