class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        size = len(s)
        dp = [[0 for j in range(size)] for i in range(size)]
        def helper(s: str, left: int, right: int) -> int:
            if left == right:
                return 0
            if left == right - 1:
                return 0 if s[left] == s[right] else 1
            
            if dp[left][right]:
                return dp[left][right]
            
            # case 1: char equal
            if s[left] == s[right]:
                dp[left][right] = helper(s, left + 1, right - 1)
                return dp[left][right]
            # case 2: char not equal: then there are two sub cases:
            # 1. only move left ptr
            # 2. only move right ptr
            dp[left][right] = 1 + min(helper(s, left + 1, right), helper(s, left, right - 1))
            return dp[left][right]
            
        
        
        return helper(s, 0, size - 1) <= k