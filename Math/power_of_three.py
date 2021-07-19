from typing import List
import math

class isPowerOfThree:
    def isPowerOfThree(self, n: int) -> bool:
        # # solution 1:
        # # Time: O(log3n)
        # # Space: O(1)
        # if n < 1:
        #     return False
        # while n % 3 == 0:
        #     n /= 3
        
        # return n == 1

        # # solution 2:
        # if n < 1:
        #     return False
        # return (math.log10(n) / math.log10(3)) % 1 == 0

        # solution 3:
        return n > 0 and 1162261467 % n == 0