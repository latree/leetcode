import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 小知识点，math.inf和 MAX_INT 不是同一个数
        # 我们需要先把两个数转换成正数，因为如果有负数的话那么最开始有一个bit 的符号位，不好操作
        # Time: O(logn)
        # Space:O(1)
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        
        # 我们需要先把两个数转换成正数，因为如果有负数的话那么最开始有一个bit 的符号位，不好操作
        sign = 1 if not (dividend < 0) ^ (divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while divisor <= dividend:
            tmp = divisor
            mul = 1
            while dividend >= (tmp << 1):
                tmp <<= 1
                mul <<= 1
            res += mul
            dividend -= tmp

        res *= sign

        if res >= MAX_INT:
            return MAX_INT
        else:
            return res

    def call_function(self) -> None:
        self.divide(10, 3)