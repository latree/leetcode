from abc import abstractproperty
from typing import Deque, List
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Solution BFS
        # Time: O(n**3) one n for queue, n**2 for slicing
        # Space:O(n)
        # word_set = set(wordDict)
        # queue = deque()
        # queue.append(0)
        # visisted = set()
        # while queue:
        #     start = queue.popleft()
        #     if start in visisted:
        #         continue
        #     for end in range(start + 1, len(s) + 1):
        #         if s[start:end] in word_set:
        #             queue.append(end)
        #             if end == len(s):
        #                 return True
        #         visisted.add(start)
        # return False
        
        # solution 2 DP
        # DP array 的物理意义是在第 idx is dp idx. dp[idx] 表示在s 的第idx-1的位置上是不是能够被截取出一个在字典里的词
        # 注意两个for 循环的方式比较特别
        # Time: O(n**3) O(n**3) one n for dp array, n**2 for slicing
        # space: O(n)
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


    def call_function(self) -> None:
        self.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
        

# c a t s a n d d o g 
# 0 1 2 3 4 5 6 7 8 9 


#                     0,0
#       (0,2)cat             (0,3)cats
#     (3,6) sand              (4,6)and
#     (7,9)dog                (7,9)dog

# [True, False, False, True, True, False, False, True, False, False, True]