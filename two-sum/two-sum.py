class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Program needs to sum two numbers and return the indeces of such
        that add up to a target:
        
        >>>twoSum([1,4,5,7], 11)
        []
        >>>twoSum([2,1,5,7], 9)
        [0, 3]
        
        """
        if not nums or len(nums) == 1:
            return []
        #Sol1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: 
                    return [i,j]
        return []
        