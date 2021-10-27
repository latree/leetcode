class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # ********************important************************
        # 第一个方法很tricky，我还是没有弄明白原理
        # How to start? There is an interview tip for bit manipulation problems: 
        # if you don't know how to start, start from computing XOR for your input data. 
        # Strangely, that helps to go out for quite a lot of problems, Single Number II, 
        # Single Number III, Maximum XOR of Two Numbers in an Array, Repeated DNA Sequences, Maximum Product of Word Lengths,
#         x, y = int(a, 2), int(b, 2)
#         while y:
#             answer = x ^ y
#             carry = (x & y) << 1
#             x,  y = answer, carry
        
#         return bin(x)[2:]

        p1, p2 = len(a) - 1, len(b) - 1
        
        res = []
        carry = 0
        while p1 >= 0 or p2 >= 0:
            d1 = ord(a[p1]) - ord('0') if p1 >= 0 else 0
            d2 = ord(b[p2]) - ord('0') if p2 >= 0 else 0
            
            value = (d1 + d2 + carry) % 2
            carry = (d1 + d2 + carry) // 2
            res.append(str(value))
            p1 -= 1
            p2 -= 1
        if carry:
            res.append(str(carry))
        
        res = res[::-1]
        return "".join(res)

    
#     1 1 1 1
#     0 0 1 0

# anwer = 1 1 0 1
# cary.   0 1 0 0

# ans   = 1 1 0 1
# cary. = 1 0 0 0


# ans =.  1 1 0 1
# cary    0 0 0 0