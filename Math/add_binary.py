class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 3点非常巧妙:
        # 1. 把a，b，carry 一起加起来 再去做% 和//
        # 2. % 就是 当前单位上的数值
        # 3. // 就是carry 到下一位的数值
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n) 
        res = []
        carry = 0
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 1:
                res.append('1')
            else:
                res.append('0')
            
            carry //= 2

        if carry == 1:
            res.append('1')
    
        return ''.join(res[::-1])