from typing import List

class productExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution: left and right product list
        # Time: O(3n) which is  O(n)
        # Space: O(3n) which is plus the result.
        N = len(nums)
        left = []
        right = [0 for _ in range(N)]
        res = [0 for _ in range(N)]
        product = 1
        for num in nums:
            product *= num
            left.append(product)
        
        product = 1
        for i in range(N - 1, -1, -1):
            product *= nums[i]
            right[i] = product
        

        for i in range(1, N - 1):
            res[i] = left[i - 1] * right[i + 1]
        res[0] = right[1]
        res[N - 1] = left[N - 2]
        return res