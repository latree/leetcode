from typing import List
import math

class romanToInt:
    def romanToInt(self, s: str) -> int:
        # # solution 1: right to left
        # roman_map = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        # temp = -1
        # res = 0
        # for i in range(len(s) - 1, 0, -1):
            
        #     if roman_map[s[i]] < temp:
        #         temp = -1
        #         res -= roman_map[s[i]]
        #     else:
        #         temp = roman_map[s[i]]
        #         res += temp
        # return res
    
        # solution 2: left to right
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        total = 0
        while i < len(s):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                total += roman_map[s[i]]
                i + 1
        return total