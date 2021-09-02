from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 这道题的solution可以有不同的方法。monotonic stack 是其中的一种。
        mono_stack = []
        res = 0
        water, cur_height, width = 0, 0, 0
        
        for i, v in enumerate(height):
            while mono_stack and v >= height[mono_stack[-1]]:
                bottom_idx = mono_stack.pop()
                if mono_stack:
                    width = i - mono_stack[-1] - 1
                    cur_height = min(height[mono_stack[-1]], v) - height[bottom_idx]
                    water = cur_height * width
                
                # 这里巧妙的用到了if condition 来剔除了开头没有凹的左半边的情况
                else:
                    water = 0
                res += water
            mono_stack.append(i)
        return res
