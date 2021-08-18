from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time:O(nlogn + n)  O(nlogn)
        # Space:O(n)
        res = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res
