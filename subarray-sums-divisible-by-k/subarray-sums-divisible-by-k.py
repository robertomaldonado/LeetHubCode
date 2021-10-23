class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        divisble_subarr = [0]*k 
        
        divisble_subarr[0] = 1
        current_sum = 0
        ans = 0 
        
        for num in nums:
            current_sum += num
            mod_index = current_sum % k
            
            if divisble_subarr[mod_index]:
                ans += divisble_subarr[mod_index]

            divisble_subarr[mod_index] += 1
            
        return ans