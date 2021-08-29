# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

  1  ->  2   ->  3  ->None
  ^      ^       ^ 
head


  1  ->  2   ->  3  ->None
  ^      ^       ^ 
head

None
  |
  1  ->  2   ->  3  ->None
  ^      ^       ^ 
head

        curr 
        curr.next = 1 
        
  1  <-  2               3  ->None
  ^      ^               ^ 
        head               next
        prev
                        curr 
        curr.next = prev
        

prev = None
curr = 1
next = 2

move it on the list. Return the new head. Head at the end of the show.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr=nxt
            head = prev
            
        return head