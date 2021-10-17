from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 这道题其实最根本的意思是从max(weight) 到 sum(weights) 这个递增的数组里找出一个min weight
        # 来符合ship within targeted days。
        # 所以这就符合binary search的条件。从一个递增数组里面找到一个target。
        def canship(cap, days):
            count = 0
            cur_cap = 0
            for weight in weights:
                if cur_cap + weight <= cap:
                    cur_cap += weight
                else:
                    count += 1
                    cur_cap = weight
            
            if cur_cap != 0:
                count += 1
            return count <= days
                
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            if canship(mid, days):
                right = mid
            else:
                left = mid + 1
        
        return right
        
        