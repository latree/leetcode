from typing import List
import random

class ShuffleArray:
    # solution 1
    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     self.original_nums = nums.copy()

    # def reset(self) -> List[int]:
    #     """
    #     Resets the array to its original configuration and return it.
    #     """
    #     return self.original_nums

    # def shuffle(self) -> List[int]:
    #     """
    #     Returns a random shuffling of the array.
    #     """
    #     tmp_array = self.nums.copy()
    #     for i in range(len(self.original_nums)):
    #         remove_idx = random.randrange(len(tmp_array))
    #         self.nums[i] = tmp_array[remove_idx]
    #         tmp_array.pop(remove_idx)
    #     return self.nums

    # solution 2
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original_nums = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()