from typing import List

class productExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Solution: left and right product list
        # # Time: O(3n) which is  O(n)
        # # Space: O(3n) which is plus the result.
        # N = len(nums)
        # left = []
        # right = [0 for _ in range(N)]
        # res = [0 for _ in range(N)]
        # product = 1
        # for num in nums:
        #     product *= num
        #     left.append(product)
        
        # product = 1
        # for i in range(N - 1, -1, -1):
        #     product *= nums[i]
        #     right[i] = product
        

        # for i in range(1, N - 1):
        #     res[i] = left[i - 1] * right[i + 1]
        # res[0] = right[1]
        # res[N - 1] = left[N - 2]
        # return res

        # 第二遍
        # 这道题需要注意的是要用到两个prefix_prod(另一种形式的prefix_sum)
        # 为这么是因为题目要求的是求除自己以外的product。那么就要分为两遍来计算。到i-1 的左边product，和从i+1开始的右边product
        n = len(nums)
        cur_prod = 1
        left = []
        right = [0] * n
        res = [0] * n
        for i in range(n):
            cur_prod *= nums[i]
            left.append(cur_prod)
        
        cur_prod = 1
        for i in range(n - 1, -1, -1):
            cur_prod *= nums[i]
            right[i] = cur_prod
        
        
        for i in range(1, n - 1):
            res[i] = left[i - 1] * right[i + 1]
        
        res[0] = right[1]
        res[n - 1] = left[n - 2]
                
        return res