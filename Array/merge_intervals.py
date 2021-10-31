from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # Time:O(nlogn + n)  O(nlogn)
        # # Space:O(n)
        # res = []
        # intervals.sort(key=lambda x: x[0])
        # for interval in intervals:
        #     if not res or res[-1][1] < interval[0]:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(interval[1], res[-1][1])
        
        # return res


        # 第二遍
        # 原理：
        # 把interval按照每一个区间的起始sort，那么我们在iterate 每一个区间的时候只需要关注当前区间和res的最后一个区间的重叠关系即可
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res