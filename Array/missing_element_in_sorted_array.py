from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        size = len(nums)
        missing_nums = [0]
        for i in range(1, size):
            num_missing = nums[i] - nums[i - 1] - 1 + missing_nums[i - 1]
            missing_nums.append(num_missing)
        
        # 另外这个special case，没想到直接在binary search 之外解决。
        if k > missing_nums[size - 1]:
            return nums[-1] + k - missing_nums[size - 1]
        
        left, right = 0, size - 1
        while left < right:
            mid = left + (right - left) // 2
            
            # condition 比较tricky，得通过举例子来决定是< 还是 <=
            if missing_nums[mid] < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - missing_nums[left - 1]

        
        
            
            