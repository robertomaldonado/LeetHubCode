"""
2  ==> [0,1,1]         ...2^1, 2^0
0 -> 0                 ...[      0 ]
1->  1                 ...[      1]
2 -> 1                 ...[ 1     0]
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countit(n):
            count = 0
            while n:
                count += n&1
                n >>= 1
            return count
        
        ans = [0]*(n+1)
        
        for i in range(n + 1):
            ans[i] = countit(i)
        return ans