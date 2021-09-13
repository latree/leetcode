class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        cur_product = x
        i = n
        # 这里最关键的地方是直接n/2的方式缩小。这样就比n-1 的方式缩小要快了很多从O(n) 变成O(logN)
        while i > 0:
            if i % 2 == 1:
                res = res * cur_product
            
            cur_product = cur_product * cur_product
            i = i // 2
        
        return res