from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(num_set, cur_set, cur, res):
            if len(cur_set) == len(num_set):
                res.append(copy.deepcopy(cur))
                return
            
            for num in num_set:
                if num not in cur_set:
                    cur.append(num)
                    cur_set.add(num)
                    dfs(num_set, cur_set, cur, res)
                    cur.pop()
                    cur_set.remove(num)

        num_set = set(nums)
        res = []
        cur_set = set()
        dfs(num_set, cur_set, [], res)
        
        return res