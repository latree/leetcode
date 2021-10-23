class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # char_map = {}
        # for ch in s:
        #     char_map[ch] = char_map.get(ch, 0) + 1
        
        # count = 0
        # for k in char_map:
        #     count += char_map[k] % 2
        
        # if count == 1 or count == 0:
        #     return True
        # return False
    

    # 第二遍
        char_map = {}
        odd_count = 0
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1
        
        for ch in char_map:
            if char_map[ch] % 2 != 0:
                odd_count += 1
        
        return odd_count <= 1
        