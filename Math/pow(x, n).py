class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        
        # res = 1
        # cur_product = x
        # i = n
        # # 这里最关键的地方是直接n/2的方式缩小。这样就比n-1 的方式缩小要快了很多从O(n) 变成O(logN)
        # while i > 0:
        #     if i % 2 == 1:
        #         res = res * cur_product
            
        #     cur_product = cur_product * cur_product
        #     i = i // 2
        
        # return res


        # 第二遍：
        # 原理，这道题还是用到了exponential increase
        # 每次以n/2的方式缩小 这样就比n-1 的方式缩小要快了很多从O(n) 变成O(logN)
        if n < 0:
            x =  1 / x
            n = -n
        res = 1
        cur_product = x
        
        i = n
        while i > 0:
            # 从做简单的case 想就好了
            # 比如2^1  和2^3，原理就是如果是一个单数次幂，那么我们要先乘以一个cur_product来补充这个单数的次幂
            if i % 2 == 1:
                res = res * cur_product
            
            cur_product = cur_product ** 2
            i = i // 2
        return res