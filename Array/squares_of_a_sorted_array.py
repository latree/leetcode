from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        res = []

        while i != j:
            if abs(nums[i]) < abs(nums[j]):
                res.append(nums[j] ** 2)
                j -= 1
            else:
                res.append(nums[i] ** 2)
                i += 1
        
        res.append(nums[i] ** 2)
        return res[::-1]

# 第二遍：
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         i, j = 0, len(nums) - 1
#         res = []
#         while i <= j:
#             if abs(nums[i]) > abs(nums[j]):
#                 res.append(nums[i] * nums[i])
#                 i += 1
#             else:
#                 res.append(nums[j] * nums[j])
#                 j -= 1
        
#         return res[::-1]