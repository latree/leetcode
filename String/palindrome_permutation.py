class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_map = {}
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1
        
        count = 0
        for k in char_map:
            count += char_map[k] % 2
        
        if count == 1 or count == 0:
            return True
        return False
    