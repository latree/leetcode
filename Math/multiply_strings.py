class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        
        m = len(num1)
        n = len(num2)
        # ******这道题最关键的地方在于这里。res size 是m+n
        res = [0] *(m + n)
        
        for i1 in range(m):
            for i2 in range(n):
                digit = int(num1[i1]) * int(num2[i2])
                # ****** 这里是第二个亮点 做乘法算数的时候其实就是在i1+i2的地方加上所有的数
                res[i1 + i2] += digit
                # 如果有进位，那么进位也需要加到下一位去，如果没有就相当于加0
                res[i1 + i2 + 1] += (res[i1+i2] // 10)
                # 如果当前位置的数超过了10 那么我们只保留做模以后的值
                res[i1 + i2] = res[i1+i2] % 10
        
        res = res[::-1]
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        res = res[i:]
        res = [str(i) for i in res]
        return "".join(res)

        
#     1 2 3
#     4 5 6
#     7 3 8
#   6 1 5
# 4 9 2
         
# 5 6 0 8 8       

