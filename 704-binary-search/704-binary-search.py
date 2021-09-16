"""
So binary search is log(n).

Splits array in two
Compare at a middle point, then reduce search each time by half
asjust start and end 
changes the side accordingly
at not found returns -1

nums = [-1,0,3,5,9,12], target = 9
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid +1
            else:
                end = mid-1
        return -1
                
            