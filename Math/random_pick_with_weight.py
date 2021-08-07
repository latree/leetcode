from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        prefix_sum = 0
        self.prefix_sum = []
        for weights in w:
            prefix_sum += weights
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # time: O(logN)
        # space: O(1)
        target = self.total_sum * random.random()
        
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            
            if target > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return right

