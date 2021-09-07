class Solution:
    def isHappy(self, n: int) -> bool:

        def get_num_sum(n):
            square_sum = 0
            for digit in str(n):
                square_sum += int(digit)**2
            return square_sum
            
        my_set = set()
        while n not in my_set and n!=1: 
            my_set.add(n) 
            n = get_num_sum(n)
            
        return n == 1