from typing import List

class maxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        # # solution 1: brute force:
        # # Time: O(n**2) run n*(n-1)/2 times
        # # Space: O(1)
        # prices_len = len(prices)
        # if not prices:
        #     return 0
        # max_profit = 0
        # for i in range(prices_len):
        #     for j in range(i + 1, prices_len):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        
        # return max_profit

        # solution 2: DP
        # Time: O(n) n is length of pridces list
        # Space: O(n) n is length of pridces list
        if not prices:
            return 0
        
        prices_len = len(prices)
        dp = [0] * prices_len
        min = prices[0]

        for i in range(1, prices_len):
            if prices[i] < min:
                min = prices[i]
            dp[i] = max(dp[i - 1], prices[i] - min)

        return dp[prices_len - 1]

    
    def call_function(self) -> None:
        print(self.maxProfit([7,1,5,3,6,4]))