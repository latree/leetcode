from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_pos(nums, target, is_left):
            n = len(nums)
            left, right = 0 , n - 1
            while left + 1 < right:
                mid  = (left + right) // 2
                if nums[mid] == target:
                    if is_left:
                        if mid - 1 < n and nums[mid - 1] < target:
                            return mid
                        
                        right = mid - 1
                    else:
                        if mid + 1 < n and nums[mid + 1] > target:
                            return mid
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return -1


        left = find_pos(nums, target, True)
        right = find_pos(nums, target, False)

        return [left, right]