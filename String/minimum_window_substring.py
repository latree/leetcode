from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 最优的解法是组成一个filtered s 只记录char 和char 的idx if char在t里面
        # 然后loop filtered s  
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        requried = len(dict_t)
        
        l, r = 0, 0
        char_formed = 0
        window_counts = {}
        
        res = (math.inf, None, None)
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                char_formed += 1
            
            while l <= r and char_formed == requried:
                char = s[l]
                
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    char_formed -= 1
                l += 1
            r += 1
            
        return "" if res[0] == math.inf else s[res[1]: res[2] + 1]