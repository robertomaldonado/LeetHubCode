# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Try recursive approach.

DFS. Using stack, as stack can be used we do the recursive approach.

      1
    /   \ 
   2    4
 / \   /  \
5   9 10  11

[5,2,9,1,10,4,11]

Inorder: Means left, parent, right
s1.
           11| 
s2.
           4,1|
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if not root: return
      cur_node = root
      s1 = []
      ans = []
      while cur_node or len(s1) != 0:
        while cur_node:
          s1.insert(0,cur_node)
          cur_node = cur_node.left
          print(cur_node)
        cur_node = s1.pop(0)
        ans.insert(0, cur_node.val)
        cur_node = cur_node.right
      return ans[::-1]
      
      """Recursive approach:
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
      """
      
      
      
      
      
      
      
      
      
      
      