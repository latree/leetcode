from typing import List

class missingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        # # solution 1: sort
        # # Time: O(nlogn)
        # # Space: O(1) or O(n)
        # nums.sort()
        # if not nums:
        #     return 0

        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        
        # return len(nums)

        # solution 2: set
        # # Time: O(n)
        # # Space: O(n)
        # num_set = set(nums)
        # n = len(nums) + 1
        # for i in range(n):
        #     if i not in num_set:
        #         return i
        
    #     # solution 3: sum
    #     # Time: O(n)
    #     # Space: O(1)
    #     sum = int((len(nums) + 1) * len(nums)/2)

    #     num_sum = 0
    #     for num in nums:
    #         num_sum += num

    #     return sum - num_sum

        # solution 4: Bit Manipulation
        # Time: O(n)
        # Space: O(1)
        missing  = len(nums)

        for i, num in enumerate(nums):
            missing ^= i ^ num

        return missing

    def call_function(self) -> None:
        self.missingNumber([3,0,1])
