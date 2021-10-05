"""
So we just consider the array of differences
Ex.: 
    prices: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    mins:   [310, 310, 275, 275, 260, 260, 260, 230, 230, 230]
    
    [0,5,0,20,0,10,30,0,25,20] =>max is 30
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far, max_profit = float('inf'), 0
        for price in prices:
            max_prof_today = price - min_so_far
            max_profit = max(max_profit, max_prof_today)
            min_so_far = min(min_so_far, price)
        return max_profit