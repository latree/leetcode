from typing import List
import math

class countPrimes:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        numbers = {}
        for p in range(2, int(math.sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        
        return n - len(numbers) - 2