from functools import lru_cache
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # # solution 1 dfs
        # 因为求的是min 所以比较容易就想到了dfs的方法
        # durations = [1, 7, 30]
        # day_set = set(days)
        
        # @lru_cache(None)
        # def dp(i):
        #     if i > 365:
        #         return 0
        #     elif i in day_set:
        #         return min(dp(i + d) + c for d, c in zip(durations, costs))
        #     else:
        #         return dp(i + 1)
        
        # return dp(1)

        # solution 2
        # dp[i] = min(dp[i], dp[max(0, d - durations)] + cost)
        # 当前的天数减去duration，如果duration 是1， 就是前一天的最小cost 再加上一个一天的cost
        # dp[i] = dp[i - 1]
        # dp 的物理意义就是到第 i天为止，能得到的最小cost
        dp = [float('inf')] * (days[-1]+1)
        dp[0] = 0
        days_set = set(days)
        durations = [1,7,30]

        for d in range(1, len(dp)):
            if d in days_set:
                for cost, duration in zip(costs,durations):
                    dp[d] = min(dp[d], dp[max(0,d-duration)]+cost)
            else:
                dp[d] = dp[d-1]
        return dp[-1]


# dp[i] = min(dp[i + 1]+cost[0], dp[i + 7] + cost[1], dp[i + 30] + cost[2])
# days = [1,4,6,7,8,20], costs = [2,7,15]

#                                1
#      2(+1)                 8(+7)                        31(+30)
    #    3(2+1)      9(8+1), 15(8+7), 38(8+30)               32(+1)
