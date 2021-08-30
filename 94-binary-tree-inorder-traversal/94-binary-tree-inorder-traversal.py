# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Try recursive approach.

BFS. Using stack, as stack can be used we do the recursive approach.

      1
    /   \ 
   2    4
 / \   /  \
5   9 10  11

-------------------|
1                  |
-------------------|

-------------------|
2, 4               |
-------------------|

-------------------|
5,9,10,11          |
-------------------|

"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      
      def _traverse(root, ans):
        if not root: 
          return
        if root.left:
          _traverse(root.left,ans)
        ans.append(root.val)
        if root.right:
          _traverse(root.right, ans)
        
      ans =[]
      _traverse(root, ans)
      return  ans
        