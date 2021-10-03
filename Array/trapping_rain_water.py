from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 这道题的solution可以有不同的方法。
        # 这个方法非常的不好想，是monotonic stack 继续优化的结果。
        # monotonic stack 的方法其实跟dp的方法差不多，需要过两遍loop， 一次从左到右，一次从右到左。
        # 但是这个方法只需要一遍loop就可以，是优化的mono_stack方法
        mono_stack = []
        res = 0
        water, cur_height, width = 0, 0, 0
        
        for i, v in enumerate(height):
            # *****************   important   **************************
            # 这里不光是用到了mono stack
            # 对于每一个i 都push 到stack 里面，只要 v >= height[mono_stack[-1]] 就会开始计算water。
            # 但是要注意的是每一次计算都是从最矮的蓄水池计算，而且计算完了以后就会pop 出去这一层的
            # 比如 [2, 1, 0, 1, 2]的蓄水池，
            # x 0   0  x
            # x x 0 x  x
            # 会先计算  x 0 x, 部分，然后这部分的i 都会pop 出stack
            # 然后再去计算 x 0   0  x这部分
            
            # 这样也不会因为左边的墙比右边的高，而漏算了这部分的蓄水
            # x    
            # x x 0 x
            # 比如以上这种情况这个代码也会cover
            # pop 的过程回溯了这种从右到左的蓄水计算
            while mono_stack and v >= height[mono_stack[-1]]:
                bottom_idx = mono_stack.pop()
                if mono_stack:
                    # 使用了width 和 cur_height 的计算方式非常巧妙.
                    width = i - mono_stack[-1] - 1
                    cur_height = min(height[mono_stack[-1]], v) - height[bottom_idx]
                    water = cur_height * width
                
                # 这里巧妙的用到了if condition 来剔除了开头没有凹的左半边的情况
                else:
                    water = 0
                res += water
            mono_stack.append(i)
        return res


# ******** second round
#         n = len(height)
#         dp_left=[0 for _ in range(n)]
#         dp_right = [0 for _ in range(n)]

#         # dp_left[i]就是i和i之前的最高的bar值。得到这个数组有一个小技巧，如果想得到dp_left那么就要从
#         # 右往左iterate，因为只有先得到的最大值，然后这个最大值之后的i位置才好直接赋值为目前最大值
#         # 反之就是dp_right[i]
#         max_left = 0
#         for i in range(n-1,-1, -1):
#             max_left = max(height[i], max_left)
#             dp_left[i] = max_left
        
#         max_right = 0
#         for i in range(n):
#             max_right = max(height[i], max_right)
#             dp_right[i] = max_right
        
#         res = 0
#         for i in range(n):
#             res += min(dp_left[i], dp_right[i]) - height[i]
        
#         return res