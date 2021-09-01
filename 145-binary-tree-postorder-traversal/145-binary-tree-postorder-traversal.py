# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Post order. 
  It means after I am done traversiing my children
  Still a bfs but it will keep in mind the tracking on a stack.
  
  
          3 
   /             \
   5              7
  /\             /  *base case
 2  1           9
 ** **         **
[2,1,5,9,7,3]

[: 3 |]
[: 7,3 |]
[: 9,7,3 |
[: ,9,7,3 |]
[: 5,9,7,3 |]
[: 2,1,5,9,7,3 |]
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      """
      def traverse_rec(self, root, ans):
        if not root: return []
        if root.left:
          traverse_rec(self, root.left, ans)
        if root.right:
          traverse_rec(self, root.right, ans)
        ans.append(root.val)
      
      ans = []
      traverse_rec(self, root, ans)
      return ans
      """
      if not root: return []
      
      s1 = []
      s2 = []
      s1.append(root)
      
      while s1:
        tmp = s1.pop()
        s2.append(tmp.val)
        
        if tmp.left:
          s1.append(tmp.left)
        if tmp.right:
          s1.append(tmp.right)
        
      return s2[::-1]
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      