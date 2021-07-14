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
        # max_sub = cur_sub = nums[0]
        # for num in nums[1:]:
        #     # if cur_sub is negative then throw it away and start with num. 
        #     cur_sub = max(num, cur_sub + num)
        #     max_sub = max(max_sub, cur_sub)
        
        # return max_sub

        # solution 3: recursion
        # Time: O(n*logn) n length of nums
        # Space: O(logn) n length of nums
        # 因为我们在把问题简化的成为左边加上中间加上右边，所以必须是三部分组合成一起的一个sum
        # 因为这个特性，所以在求左边和右边的最大sum的时候我们可以直接使用cur+= nums[i]
        # 因为他必须是连贯的，所以左边从中间向左累加，右边从中间向右累加
        def helper(nums: List[int], left: int, right:int) -> int:
            if left > right:
                return -math.inf
            
            cur_sub = max_left_sub = max_right_sub = 0
            mid = (left + right) // 2

            for i in range(mid - 1, left - 1, -1):
                cur_sub += nums[i]
                max_left_sub = max(cur_sub, max_left_sub)

            cur_sub = 0
            for i in range(mid + 1, right + 1):
                cur_sub += nums[i]
                max_right_sub = max(cur_sub, max_right_sub)
            
            max_combine = nums[mid] + max_left_sub + max_right_sub
            left_half = helper(nums, left, mid - 1)
            right_half = helper(nums, mid + 1, right)

            return max(max_combine, left_half, right_half)
        return helper(nums, 0, len(nums) - 1)
        
    def call_function(self) -> None:
        print(self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))