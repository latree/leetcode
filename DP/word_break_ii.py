from typing import List
from collections import Counter

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 在设立两个指针的时候是先设立右边界的指针，然后遍历左边界的指针去找结果
        # 每一个dp[j:i]都有且只有一个在字典里的词。
        # dp[i]的物理意义是：s[0:i]这个区间里，所有符合条件的解
        # Time:O(n**2 + 2**n + w)  n**2 是两层循环，2**n 是prefix 长度为k的情况下最多有2**(k-1) 个解
            # 所以在 tmp_res.append((sub_string + ' ' + s[j:i]).strip()) 会花费2**n的时间
            # 最后一个w是建立word_set需要的时间。
        # Space: O((2**n)*n + n**2 + w) (2**n)*n 2**n 个解，每个解需要n个长度的string
            # n**2 不是特别明白 
            # 最后一个w是建立word_set需要的时间

        # second round notes:
        # dp[i] till index i, there are several solutions setence. 
        # dp[i] = dp[i].append(dp[j]+s[j:i]  if dp[j] exist and s[j:i] in wordDictSet)
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []

        word_set = set(wordDict)
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        for i in range(1, len(s) + 1):
            tmp_res = []
            for j in range(i):
                if s[j: i] in word_set:
                    for sub_string in dp[j]:
                        tmp_res.append((sub_string + ' ' + s[j:i]).strip())
            dp[i] = tmp_res
        
        return dp[len(s)]

    def call_function(self) -> None:
        self.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])