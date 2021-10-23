class Solution:
    def climbStairs(self, n: int) -> int:
        # def climber(i, n):
        #     if i > n: return 0
        #     if i == n: return 1
        #     return climber(i + 1, n) + climber(i + 2, n)
        # return climber(0, n, memo)
        
        def climber(i, n, mem):
            
            if i > n: return 0
            if i == n: return 1
            if mem[i] > 0: return mem[i] 
            
            mem[i] = climber(i + 1, n, mem) + climber(i + 2, n, mem)
            return mem[i]
        
        mem = [0]*(n + 1)
        return climber(0, n, mem)