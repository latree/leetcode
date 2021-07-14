import math
from typing import List

class Rob:
    def rob(self, nums: List[int]) -> int:
        # solution 1: DP
        if not nums:
            return 0
        
        if len(nums) < 3:
            max_res = 0
            for num in nums:
                max_res = max(max_res, num)
            return max_res
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]

        res = max(dp[0], dp[1], dp[2])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-3]+nums[i])
            res = max(res, dp[i])
            
        return res

    def call_function(self) -> None:
        print(self.rob([1,  2, 3,  1]))