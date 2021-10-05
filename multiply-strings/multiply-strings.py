"""
Notes:
we plan to use it as an array

12, 12 = 144

  1 2
x 1 2
_____
  2 4
1 2
+____
144
10 * 10 = 100

[0,0,0,0] => n + m
[1,2] i = 0
[1,2] j = 0
 Use // and %
 
 [0,1,4,4]  //10=> i+j
            %10 => += i+j+1
Erase trailing zeroes

"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sign = -1 if (int(num1[0]) < 0) ^ (int(num2[0]) < 0) else 1
        
        ans = [0] * (len(num1) + len(num2))
        num1 = [int(x) for x in num1]
        num2 = [int(y) for y in num2]
        
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                ans[i+j+1] += num1[i] * num2[j]
                ans[i+j] += ans[i+j+1]//10
                ans[i+j+1] = ans[i+j+1]%10
                
        ans = ans[next((i for i, x in enumerate(ans) if x!=0), len(ans)):] or [0]
        ans = [str(c) for c in ans]
        ans = "".join(ans)
        return ans