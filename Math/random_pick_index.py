from typing import List
import random 

class Solution:
    # def __init__(self, nums: List[int]):
    #     self.nums_map = {}
    #     for i, num in enumerate(nums):
    #         self.nums_map[num] = self.nums_map.get(num, []) + [i]

    # def pick(self, target: int) -> int:
    #     n = len(self.nums_map[target])
    #     if n > 1:
    #         idx = random.randint(0, n - 1)
    #         return self.nums_map[target][idx]
    #     else:
    #         return self.nums_map[target][0]
 

# 第二遍：
    def __init__(self, nums: List[int]):
        self.idx_map = {}
        for i in range(len(nums)):
            if nums[i] not in self.idx_map:
                self.idx_map[nums[i]] = []
            self.idx_map[nums[i]].append(i)

    def pick(self, target: int) -> int:
        target_idx = random.randint(0, len(self.idx_map[target]) - 1)
        return self.idx_map[target][target_idx]