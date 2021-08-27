"""

Palindrome number:

 121 => true
 
 12321 => true
 
 1 2 3 2 1 
 ^       ^
 
 1 2 3 2 1 
   ^   ^
   
 1 2 3 2 1 
     ^
     
 1 2 3 2 1 
 ^       ^
 
 1 2 2 1 
 ^     ^
 
 1 2 2 1 
   ^ ^
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(str(x)) == 1: return True
        
        x=str(x)
        l, r = 0, len(x)-1
        mid = r/2
        while r >= mid:
            if x[l] != x[r]:
                return False
            l+=1
            r-=1
        return True
    