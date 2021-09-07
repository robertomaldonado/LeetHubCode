class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        ans.append([])
        if not nums:
            return ans

        for num in nums:
            ans.extend(
                [curr + [num] for curr in ans]
            )
        
        return ans