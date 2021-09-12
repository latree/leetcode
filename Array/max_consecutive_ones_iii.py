from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 需要注意的是sliding window， 当zeros 超过k，不是一下reset，而是一步一步挪动l
        if not nums:
            return 0
        l = 0
        zeros = 0
        res = 0
        for i in range(len(nums)):
            if not nums[i]:
                zeros += 1
                
            while l <= i and zeros > k:
                if not nums[l]:
                    zeros -= 1
                l += 1

            res = max(i - l + 1, res)
                    
        return res

                