class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n*k == 0:
            return 0
        
        max_len = 0
        l, r = 0,0
        ch_idx_map = {}
        max_len = 1
        while r < len(s):
            ch_idx_map[s[r]] = r
            r += 1
            
            if len(ch_idx_map) > k:
                to_del = min(ch_idx_map.values())
                del ch_idx_map[s[to_del]]
                l = to_del + 1
            
            max_len = max(max_len, r - l)
        
        return max_len