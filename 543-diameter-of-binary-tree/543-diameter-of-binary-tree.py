class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Given a binary tree, you need to compute the length of the diameter of the tree.
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
        This path may or may not pass through the root.
        """
        self.ans = 0 
        
        def depth(root):
            if not root : return 0 
            
            l_h = depth(root.left)
            r_h = depth(root.right)
            if (self.ans < r_h + l_h):
              self.ans = (r_h + l_h) 
            else:
              self.ans
            return max((l_h, r_h))+1
            
        depth(root)
        return self.ans