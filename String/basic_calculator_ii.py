class Solution:
    def calculate(self, s: str) -> int:
        # m = len(s)
        # stack = []
        # cur_ops = "+"
        # cur_num = 0
        # for i in range(m):
        #     cur_char =s[i]
        #     if cur_char.isdigit():
        #         cur_num = cur_num * 10 + int(cur_char)
        #     if not cur_char.isdigit() and cur_char != " " or i == m - 1:
        #         if cur_ops == '+':
        #             stack.append(cur_num)
        #         elif cur_ops == '-':
        #             stack.append(-cur_num)
        #         elif cur_ops == '*':
        #             stack.append(stack.pop() * cur_num)
        #         elif cur_ops == '/':
        #             dividend = stack.pop()
        #             tmp_res = -(-dividend // cur_num) if dividend < 0 else dividend // cur_num
        #             stack.append(tmp_res)
                
        #         cur_num = 0
        #         cur_ops = cur_char
        
        # res = 0
        # while stack:
        #     res += stack.pop()

        # return res

# 第二遍
        # 原理：
        # 关键的地方是cur_ops是记录的前一个的运算符，不是当下的运算符
        # 每个循环末尾要reset cur_num 和把当前的operation 传递到cur_ops里
        # 如果碰到数字，那么先得到完整的数字
        # 如果碰到符号，那么就分4种情况讨论
        # 1. 加号就直接append
        # 2. 减号append负的数字，因为这里的cur_ops是前一个的符号，而不是当前符号
        # 3. 乘号就先把top of stack 做乘法然后push回去
        # 4. 除法跟乘法一样，只不过有一个小的corner case 我在下面的注释解释了
        stack = []
        cur_ops = "+"
        cur_num = 0
        m = len(s)
        
        for i in range(len(s)):
            if s[i].isdigit():
                cur_num = cur_num * 10 + int(s[i])
            if not s[i].isdigit() and s[i] != " " or i == m - 1:
                ch = s[i]
                if cur_ops == "+":
                    stack.append(cur_num)
                elif cur_ops == "-":
                    stack.append(-cur_num)
                elif cur_ops == "*":
                    stack.append(stack.pop() * cur_num)
                elif cur_ops == "/":
                    dividend = stack.pop()
                    # 这里很tricky，Python里面dividend // cur_num, 这个// 一直是向下round的结果。3//5 = 0  -3//5 = -1
                    # 所以这里必须要分dividend 是大于0还是小于0两种情况
                    tmp = -(-dividend // cur_num) if dividend < 0 else dividend // cur_num
                    stack.append(tmp)
                    
                cur_num = 0
                cur_ops = ch
        
        res = 0
        while stack:
            res += stack.pop()
        
        return res


    def call_function(self) -> None:
        self.calculate("14-3/2")


# "3 - 2 * 2 + 1"
#              i
# stack = [3, -4 ]

# cur_ops = +
# cur_num = 1
