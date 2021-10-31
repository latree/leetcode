import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
# # 小知识点，math.inf和 MAX_INT 不是同一个数
# # 我们需要先把两个数转换成正数，因为如果有负数的话那么最开始有一个bit 的符号位，不好操作
#         # Time: O(logn)
#         # Space:O(1)
#         # Constants.
#         MAX_INT = 2147483647        # 2**31 - 1
        
#         # 我们需要先把两个数转换成正数，因为如果有负数的话那么最开始有一个bit 的符号位，不好操作
#         sign = 1 if not (dividend < 0) ^ (divisor < 0) else -1
#         dividend = abs(dividend)
#         divisor = abs(divisor)

#         res = 0
#         while divisor <= dividend:
#             tmp = divisor
#             mul = 1
#             while dividend >= (tmp << 1):
#                 tmp <<= 1
#                 mul <<= 1
#             res += mul
#             dividend -= tmp

#         res *= sign

#         if res >= MAX_INT:
#             return MAX_INT
#         else:
#             return res


# 第二遍：
        # 原理：
        # 1. 一个整数每做一次bit left shift 就相当于乘以2
        # 2. 19 除以 3， 就相当于 3* (2**2 + 2**1), 而 (2**2 + 2**1) 就是我们要的答案
        #     每一次以2的次方的网上找到小于19的最大值， 3*(2**3) > 19 所以第一次找到 3*(2**2) 
        #     3*(2**3) == 12. 19 - 12 = 7, 然后3*(2**1) ==6
        # 小技巧：
        #  1 if not (dividend < 0) ^ (divisor < 0 ) else -1
        #  这是用来找到除数和被除数的符号是不是相同的。这里巧妙的运用到了一个bit or operation。
        #  先用除数和被除数与0 作比较的结果，如果这两个结果做或运算最后得1 那说明他们每一位都是相同的。那么就是符号相同
        #  反之符号不同
        
        sign = 1 if not (dividend < 0) ^ (divisor < 0 ) else -1
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        res = 0
        while abs_divisor <= abs_dividend:
            tmp = abs_divisor
            mul = 1
            
            while abs_dividend >= (tmp << 1):
                tmp = tmp << 1
                mul = mul << 1
            
            res += mul
            abs_dividend -= tmp
        
        res *= sign
        
        if res >= 2**31 -1:
            return 2**31 - 1
        else:
            return res


    def call_function(self) -> None:
        self.divide(10, 3)