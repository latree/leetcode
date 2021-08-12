from typing import List
import random 

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_map = {}
        for i, num in enumerate(nums):
            self.nums_map[num] = self.nums_map.get(num, []) + [i]

    def pick(self, target: int) -> int:
        n = len(self.nums_map[target])
        if n > 1:
            idx = random.randint(0, n - 1)
            return self.nums_map[target][idx]
        else:
            return self.nums_map[target][0]
 

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)