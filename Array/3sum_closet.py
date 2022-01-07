from typing import List
import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # diff = math.inf
        
        # for i in range(len(nums)):
        #     l, h = i + 1, len(nums) - 1
            
        #     while l < h:
        #         three_sum = nums[i] + nums[l] + nums[h]
                
        #         if abs(target - three_sum) < abs(diff):
        #             # 这里整数和负数代表了这个diff 离target是从左右多远的距离，还是从右有多远的距离。
        #             # 不可以是abs，如果是abs那么在决定增加low，还是降低high的时候就会出错。
        #             diff = target - three_sum
        #         # 这里应该是和target 做比较，如果three_sum 小于target，那么就是挪动l
        #         if three_sum < target:
        #             l += 1
        #         else:
        #             h -= 1
        #     if diff == 0:
        #         break
        # return target - diff


# 第二遍
        # 因为这里不是要求是连续的三个nums的元素。那么我们就用最基础的方法：每一个循环固定一个变量，然后根据计算来左右移动剩下的两个变量。这个前提必须是一个sorted list
        nums.sort()
        diff = -math.inf
        
        for i in range(len(nums)):
            l, h = i + 1, len(nums) - 1
            
            while l < h:
                three = nums[i] + nums[l] + nums[h]
                
                if abs(target - three) < abs(diff):
                    # ****** important ********
                    # 这里还是错了
                    # 这里整数和负数代表了这个diff 离target是从左右多远的距离，还是从右有多远的距离。
                    # 不可以是abs，如果是abs那么在决定增加low，还是降低high的时候就会出错。
                    diff = target - three
                
                if three < target:
                    l += 1
                
                else:
                    h -= 1
            
            if diff == 0:
                break
                
        return target - diff