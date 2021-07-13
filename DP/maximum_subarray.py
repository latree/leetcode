import math
from typing import List

class maxSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        # # solution 1: brute force
        # # Time: O(n**2)
        # # space: O(1)
        # max_sub = -math.inf
        # for i in range(len(nums)):
        #     cur_sub = 0
        #     for j in range(i, len(nums)):
        #         cur_sub += nums[j]
        #         max_sub = max(max_sub, cur_sub)

        # return max_sub

        # solution 2: DP
        # # Time: O(n) 
        # # Space: O(1)

        max_sub = cur_sub = nums[0]

        for num in nums[1:]:
            # if cur_sub is negative then throw it away and start with num. 
            cur_sub = max(num, cur_sub + num)
            max_sub = max(max_sub, cur_sub)
        
        return max_sub

    def call_function(self) -> None:
        print(self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))