class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        curr = 1
        for i in range(1,len(nums)):
            if nums[curr-1] != nums[i]:
                nums[curr] = nums[i]
                curr+=1
        return curr