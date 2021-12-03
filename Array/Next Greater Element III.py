class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 刚开始没有搞清楚题目的问题在哪里
        # 1. 首先要从后面出发找出结束递增的idx。
        # 2. 然后以这个idx出发，从左往右找出最后以后大于这个idx值的 idx 
        # 3. swap 两个idx
        # 4. 把从step 1 开始的idx 之后的所有元素都reverse
        
        digits = []
        s = str(n)
        for i in range(len(s)):
            digits.append(s[i])
        
        i = len(digits) - 1
        
        while i - 1 >= 0 and digits[i - 1] >= digits[i]:
            i -= 1
        
        if i == 0:
            return -1

        j = i
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1
        
        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        digits[i:] = digits[i:][::-1]
        
        res = int("".join(digits))
        return res if res < 2**31 else -1

    
    
    
