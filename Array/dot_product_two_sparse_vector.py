from typing import List

class SparseVector:
    # solution 1:
    # def __init__(self, nums: List[int]):
    #     self.vector = nums.copy()

    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     return sum(i[0] * i[1] for i in zip(self.vector, vec.vector))

    # solution 2:
    def __init__(self, nums: List[int]):
        self.non_zero = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.non_zero[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in vec.non_zero:
            if i in self.non_zero:
                res += self.non_zero[i] * vec.non_zero[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)