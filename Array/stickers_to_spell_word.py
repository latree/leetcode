from typing import List
import math
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # conver stickers to a counter for each char in each sticker
        count_stickers = []
        for sticker in stickers:
            temp_count = {}
            for ch in sticker:
                temp_count[ch] = temp_count.get(ch, 0) + 1
            count_stickers.append(temp_count)
        
        # dp 代表在当前这个剩余的chars 的情况，最少需要用到的sticker的数量。
        dp = {}
        def dfs(t, sticker):
            if t in dp:
                return dp[t]
            
            # 因为最开始call dfs的function的时候pass的是一个空的dict
            # 所以在最开始的时候res应该设为0， 但是在之后的运算继续call dfs 以后
            # 那么至少会有当前的sticker 算在内，所以res 会设置成为1
            res = 1 if sticker else 0
            # 计算剩余的chars 是什么
            remain_t = ""
            for ch in t:
                if ch in sticker and sticker[ch] > 0:
                    sticker[ch] -= 1
                else:
                    remain_t += ch
            
            # 这里有三个重要的砍枝的步骤：
            # 第一个： if remain_t， 如果没有remain_t那么都不需要继续运算
            # 第二个：if t in dp， 说明当前的remain_t 的最少sticker数已经运算过了
            # 第三个：if remain_t[0] not in count_sticker，如果第一个剩余的字母都不在接下来用的sticker
            #     里，那么我们当然不需要这个分枝。 for example：
            #     thehat -> with(ehat) -> with?(砍掉，因为e不在with里)
            if remain_t:
                min_used = math.inf
                for count_sticker in count_stickers:
                    if remain_t[0] not in count_sticker:
                        continue
                    min_used = min(min_used, dfs(remain_t, count_sticker.copy()))
                
                dp[remain_t] = min_used
                res += min_used
            return res
            
        res = dfs(target, {})
        return res if res != math.inf else -1
        
        
        
    #                                                 thehat
    #                 with(ehat)                          example              science
    # with?nope       example(_h_t)   science(_hat)
    #             with()              with(__a_)
    #                                 example()