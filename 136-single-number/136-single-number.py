class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # answer = 0
        # for num in nums:
        #     #All the numbers that have a pair will zero out!!!
        #     answer ^= num #Awesome idea!!! 
        # return answer
        set_num = set()
        for num in nums:
            if num in set_num:
                set_num.remove(num)
            else:
                set_num.add(num)
        return set_num.pop()
    