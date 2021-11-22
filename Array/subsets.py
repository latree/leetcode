import copy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 这道题开始没有想到的地方是在于跟普遍的recursion不一样的是开都的stop condition没有了
        # 没有的原因是因为这个recursion的call 本身就是有限的。
        # 从最开始从idx 0 开始遍历。因为每一次recursive call 都会从start 开始再遍历。
        # 所以如果拿3个元素的list 遍历举例子的话，遍历应是这样的
        # 1， 12， 123， 13， 2， 23， 3
        # 这就是所有遍历的情况。本身的stop condition就是在每一层的call里面for循环遍历结束的时候
        
        def dfs(nums, res, cur, start):
            res.append(copy.deepcopy(cur))
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(nums, res, cur, i + 1)                
                cur.pop()

        res = []
        cur = []
        dfs(nums, res, cur, 0)
        return res 
        

            #                                                 []
            #          [1]                                     [2]                                       [3]
            # [1, 2]      [1, 3 ]                             [2, 3]
            # [1, 2, 3]   