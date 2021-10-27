class addStrings:
    def addStrings(self, num1: str, num2: str) -> str:
        # # solution 1:
        # def to_int(num: str) -> int:
        #     res = 0
        #     for i in range(len(num) - 1, -1, -1):
        #         res += (10 ** i) * int(num[len(num) - 1 - i])
        #     return res
        
        # return str(to_int(num1) + to_int(num2))

        # # solution 2:
        # # Time: O(n) n is max(len(num1), len(num2))
        # # Space: O(n)
        # carry = 0
        # res = []
        # p1, p2 = len(num1) - 1, len(num2) - 1
        # while p1 >= 0 or p2 >= 0:
        #     x1 = ord(num1[p1]) - ord('0') if p1 >=0 else 0
        #     x2 = ord(num2[p2]) - ord('0') if p2 >=0 else 0

        #     value = (x1 + x2 + carry) % 10
        #     carry = (x1 + x2 + carry) // 10
        #     res.append(value)
        #     p1 -= 1
        #     p2 -= 1
        # if carry:
        #     res.append(carry)
        # return "".join(str(i) for i in res[::-1])
    

        # 第二遍
        # 刚开始开顾虑num1 如果加完了怎么办?
        # 应该是 while p1 >= 0 or p2 >= 0:   还是 while p1 >= 0 and p2 >= 0:?
        # 如果在那一位上没有数字，那么直接用0 补充就可以了。所以应该用or
        p1, p2 = len(num1) - 1, len(num2) - 1
        
        res = []
        carry = 0
        while p1 >= 0 or p2 >= 0:
            d1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            d2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            value = (d1 + d2 + carry) % 10
            carry = (d1 + d2 + carry) // 10
            res.append(str(value))
            p1 -= 1
            p2 -= 1
        if carry:
            res.append(str(carry))
        
        res = res[::-1]
        return "".join(res)
