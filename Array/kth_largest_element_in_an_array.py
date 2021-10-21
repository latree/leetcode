from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution 1 heap
        # time:O(n*logk)
        # space: O(k)
        # return heapq.nlargest(k, nums)[-1]

        #solution 2
        h = []
        for value in nums:
            heapq.heappush(h, value)
        res = [heapq.heappop(h) for i in range(len(h))]
        
        return res[len(nums) - k]