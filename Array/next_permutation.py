from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n)
        # Space: O(n)
        # 1 从后开始找到第一个不递增的数 i
        # 2 从后开始找到第一个比 i大的数
        # 3 swap
        # 4 把 i之后的位置都倒过来
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]

        start = i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



# # 第二遍心得：
#         if len(nums) < 2:
#             return nums
#         i, j = len(nums) - 2, len(nums) - 1
#         while i >= 0 and nums[i] >= nums[j]:
#             i -= 1
#             j -= 1
        
#         if j == 0:
#             return nums.sort()
        
#         while j < len(nums) - 1:
#             if nums[i]  < nums[j] and nums[i] >= nums[j + 1]:
#                 break
#             j += 1        
        
#         nums[i], nums[j] = nums[j], nums[i]
        
#         temp = nums[i+1:len(nums)]
#         nums[i+1:] = temp[::-1]
        
#         # ******************   记住array slicing 是Lst[ Initial : End : IndexJump ]
#         # 这是不用temp的slicing的方法，不过太难理解了。如果真的用的话还是用上面的比较好
#         # 如果reverse array的话那么array slicing的start 和end 概念也要reverse。
#         # nums[i+1:] = nums[len(nums) - 1:i:-1]
        
#         return nums

# 第三遍
#         # 1,2, 3, 1, 2
#         # 1. from right to left, find the longest decending part
#         # 2. get the pivot, which is one more left on the left side of deecending subarray
#         # 3. start from pivot, from left to right, find the last element(b) which is greater than pivot
#         # 4. swap pivot and b values
#         # 5. sort as increasing order from next pivot to the end of element

#         if len(nums) < 2:
#             return nums
        
#         i, j = len(nums) - 2, len(nums) - 1
        
#         while i >= 0 and nums[i] >= nums[j]:
#             i -= 1
#             j -= 1
        
#         # if j ==0 means entire array is decending order
#         if j == 0:
#             return nums.sort()

#         # now i is pivot, find the rightmost successor
#         while j < len(nums) - 1:
#             if nums[i] < nums[j] and nums[i] >= nums[j + 1]:
#                 break
#             j += 1
        
#         # swap
#         nums[i], nums[j] = nums[j], nums[i]
        
#         temp = nums[i + 1:len(nums)]
#         nums[i+1:] = temp[::-1]
        
#         return nums