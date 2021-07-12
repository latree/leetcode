from typing import List

class climbStairs:
    def climbStairs(self, n: int) -> int:
#         # solution 1 dp
#         if n == 1:
#             return 1
#         dp = [0] * n
#         dp[0] = 1
#         dp[1] = 2
#         for i in range(2, n):
#             dp[i] = dp[i - 1] + dp[i -2]
        
#         return dp[n-1]

#         # solution 2 straight forward recursion
#         # Time: O(2**n) 2 is number of different steps move. In this question, it would be 1 and 2. Total 2. 
#         # n is number of steps
#         # space: O(n) n would be the depth of the Tree. so log(2**n) n 
#         def helper(step_type: int, steps: int) -> int:
#             if step_type > steps:
#                 return 0
#             if step_type == steps:
#                 return 1
            
#             return helper(step_type + 1, steps) + helper(step_type + 2, steps)
            
#         return helper(0, n)

        # # solution 3 straight forward recursion with memory steps
        # # Time: O(n) because if remove the duplicate recursion call since we have 'record' history calculation
        # # Spcae: O(n) because it still needs to go to n depth of tree of recursion call
        # def helper(step_idx: int, steps: int, record: List[int]) -> int:
        #     if step_idx > steps:
        #         return 0
        #     if step_idx == steps:
        #         return 1
            
        #     if record[step_idx] > 0:
        #         return record[step_idx]
        #     record[step_idx] = helper(step_idx + 1, steps, record) + helper(step_idx + 2, steps, record)
        #     return record[step_idx]
        # return helper(0, n, [0] * n)
        
        # solution 4 Fibonacci Number
        if n == 1:
            return 1

        first, second = 1, 2
        for i in range(3, n + 1):
            next = first + second
            first = second
            second = next
        
        return second