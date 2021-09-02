from typing import List

def nextGreaterElement(self, nums: List[int]) -> List[int]:
    # will store pair [value, idx]
    mono_stack = []

    res = [-1] * len(nums)
    for i, value in enumerate(nums):
        while mono_stack and value >= mono_stack[-1][0]:
            cur_v, cur_i = mono_stack.pop()
            res[cur_i] = cur_v
        
        mono_stack.append([value, i])
    
    return res


def solve(nums: List[int], window: int):
    mono = deque()
    n = len(nums)
    res = [] # or some initial values like 0 (for finding a max) or 1 << 30 (for finding a min)

    for i in range(n):
        while mono and nums[mono[-1]] ? nums[i]: # ? can be one of >, <, >=, <=
            mono.pop()  # pop from top, like monotonic stacks
            # if we can update max/min/res here, then maybe monotonic stack is enough

        while mono and nums[mono[0]] ? nums[i]:
            # update max/min/res here, this is why we need a queue instead of a stack
            mono.popleft()

        if check(mono[0]):
            pass
            # or we can update max/min/res here, based on mono[0]

        mono.append(i)


    return res

    # https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/245363/A-template-for-monotonic-queue-problems
    # https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%B3%BB%E5%88%971.md