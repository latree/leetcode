from typing import List
import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        
        for i in range(len(nums)):
            l, h = i + 1, len(nums) - 1
            
            while l < h:
                sum = nums[i] + nums[l] + nums[h]
                
                if abs(target - sum) < abs(diff):
                    # 这里整数和负数代表了这个diff 离target是从左右多远的距离，还是从右有多远的距离。
                    # 不可以是abs，如果是abs那么在决定增加low，还是降低high的时候就会出错。
                    diff = target - sum
                if sum < diff:
                    l += 1
                else:
                    h -= 1
            if diff == 0:
                break
        return target - diff