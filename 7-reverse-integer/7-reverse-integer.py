"""
Input: x 
Return: x reversed

Input: x = -123
Output: -321

First we need to check for the sign/
After that we make it a positive.
Now we can begin storing the //10 of the number and keep updaeing it until we have nothing left of the numer

x = -123
sign = -1

x=123
123 % 10 => 3. [3]    
x = 123//10 = 12
12 => 2 [3,2]
1 => 1  [3,2,1]
Concat based on position
multiply for my sign
0. 
join the ejected numbers, we may have them in a list for ease.
"""

class Solution:
    """
    If converting to str is allowed:

        sign = 1
        if x < 0:
          sign = -1
          x = sign * x 
          
        str_digit = [digit for digit in str(x)][::-1]
        
        num = sign * int("".join(str_digit))
        if  num > (2**31) -1 or num < -1 * (2**31) -1:
          return 0
        return num
    """
    def reverse(self, x: int) -> int:
        if not x or x == 0:
            return 0
        sign = 1
        num_list = []
        rev_x = 0
        if x<0:
            sign=-1
            x=x*sign
            
        while x != 0:
            cur = x%10
            num_list.append(cur)
            x=x//10
            
        pos = len(num_list)-1
        for dig in num_list:
            rev_x += dig*10**pos
            pos -= 1
        rev_x = rev_x * sign
        
        if rev_x < -2**31 or rev_x > 2**31-1:
            return 0
        return rev_x
        