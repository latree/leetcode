from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 这是最基础的monotonic stack 问题
        # pair [temp, idex]
        mono_stack = [] 
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while mono_stack and t > mono_stack[-1][0]:
                cur_t, cur_i = mono_stack.pop()
                res[cur_i] = i - cur_i
            mono_stack.append([t, i])
        
        return res
                