from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # # 这道题也需要画出recursion tree
        # # 每一个node 应该是bucket，而且表示了把当前index 的nums的数字放进bucket以后的状态，
        # # 每一个node会有四个分枝，代表把当前的数字分别放进四个bucket里面
        # # 一共有len(nums) 层的tree
        # # 剪枝的过程就是要把当前大于target的bucket以及之后的树枝都减掉
        # def dfs(nums, idx, bucket, target):
        #     if idx == len(nums):
        #         for ele in bucket:
        #             if ele != target:
        #                 return False
        #         return True
            
        #     for i in range(len(bucket)):
                
        #         if bucket[i] + nums[idx] > target:
        #             continue
                
        #         bucket[i] += nums[idx]
        #         if dfs(nums, idx + 1, bucket, target):
        #             return True
        #         bucket[i] -= nums[idx]
            
        #     return False
        
        # if k > len(nums):
        #     return False
        # if sum(nums) % k != 0:
        #     return False
        
        # nums.sort(reverse=True)
        
        # bucket = [0] * k
        
        # target = sum(nums) / k
        
        # return dfs(nums, 0, bucket, target)

        # solution 2: 以桶的视角遍历所有数字
            
#                                                                               [][][][]
#        [4][][][]             [3][][][]                         [2][][][]                        [3][][][]                  [5][][][]                      [2][][][]                     [1][][][] 
        
#         |
#     [4+1][][][]        [3+2][][][]   [3+2][][][]            [2][][][] 
        
        def dfs(nums, used, bucket, k, target, start):
            if k == 0:
                return True
            
            if bucket == target:
                return dfs(nums, used, 0, k - 1, target, 0)
    
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if bucket + nums[i] > target:
                    continue
                used[i] = True
                
                if dfs(nums,used, bucket+nums[i], k, target, i + 1):
                    return True
                used[i] = False
            
            return False
        if k > len(nums):
            return False
        if sum(nums) % k != 0:
            return False
        target = sum(nums) / k
        used = [False] * len(nums)
        return dfs(nums, used, 0, k, target, 0)
        

        