"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        
        q = collections.deque([])
        q.append((root, 0))
        pre_level = -1
        pre_node = None
        
        while q:
            node, level = q.popleft()
            
            if pre_level != level:
                pre_level = level
            #Start next level
            else:
            # `   on level
                pre_node.next = node
            
            if node.left is not None:
                q.append((node.left, level+1))
                q.append((node.right, level+1))
            
            pre_node = node
        return root