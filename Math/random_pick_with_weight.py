from typing import List
import random

class Solution:

    # def __init__(self, w: List[int]):
    #     prefix_sum = 0
    #     self.prefix_sum = []
    #     for weights in w:
    #         prefix_sum += weights
    #         self.prefix_sum.append(prefix_sum)
    #     self.total_sum = prefix_sum

    # def pickIndex(self) -> int:
    #     # time: O(logN)
    #     # space: O(1)
    #     target = self.total_sum * random.random()
        
    #     left, right = 0, len(self.prefix_sum) - 1
    #     while left < right:
    #         mid = (left + right) // 2
            
    #         if target > self.prefix_sum[mid]:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return right


    # 第二遍
    # 这道题开始的时候花了很长的时间理解题意
    # 其实本质就是我们要create 一个权重的数组，然后随机产生一个1 到total的随机数
    # 然后找到这个随机数落到这个权重数组的哪里。这样就能保证这个权重的随机概率了。
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        cur_sum = 0 
        for weight in w:
            cur_sum += weight
            self.prefix_sums.append(cur_sum)
        self.total = cur_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            # 这里还开始的时候写错了。如果target 大于当前权重的边界值的时候
            # 我们应该果断忽略掉当前合格权重的左侧。因为这个target不可能掉在
            # 左侧那些权重值里
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left