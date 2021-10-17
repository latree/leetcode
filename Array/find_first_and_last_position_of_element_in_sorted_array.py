from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     def find_pos(nums, target, is_left):
    #         n = len(nums)
    #         left, right = 0 , n - 1
    #         while left + 1 < right:
    #             mid  = (left + right) // 2
    #             if nums[mid] == target:
    #                 if is_left:
    #                     if mid - 1 < n and nums[mid - 1] < target:
    #                         return mid
                        
    #                     right = mid - 1
    #                 else:
    #                     if mid + 1 < n and nums[mid + 1] > target:
    #                         return mid
    #                     left = mid + 1
    #             elif nums[mid] < target:
    #                 left = mid
    #             else:
    #                 right = mid
    #         return -1


    #     left = find_pos(nums, target, True)
    #     right = find_pos(nums, target, False)

    #     return [left, right]


        # 第二遍：
        # ************************** important!!!!! ********************************
        # 这道题非常好，是典型的一个例子的二分法的两种方式；找最左侧的符合条件的值，和找最右侧符合条件的值
        # 上半部分是用来找最左侧的符合条件的值，下半部分是找最右侧符合条件的值。
        # 我还需要看一下对于二分法的总结。我总是觉得还有点地方没有融会贯通
        res = [-1, -1]
        if not nums:
            return res
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        
        if nums[left] != target:
            return res
        res[0] = left
        
        # 这里可以只重新设置right，继续沿用left的值
        # 因为left就是我们要找的左边界，我们只用关心right的边界能不能找到
        right = len(nums) - 1
        # left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        res[1] = right
        
        return res