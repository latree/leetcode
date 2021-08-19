class Solution:
    def calculate(self, s: str) -> int:
        m = len(s)
        stack = []
        cur_ops = "+"
        cur_num = 0
        for i in range(m):
            cur_char =s[i]
            if cur_char.isdigit():
                cur_num = cur_num * 10 + int(cur_char)
            if not cur_char.isdigit() and cur_char != " " or i == m - 1:
                if cur_ops == '+':
                    stack.append(cur_num)
                elif cur_ops == '-':
                    stack.append(-cur_num)
                elif cur_ops == '*':
                    stack.append(stack.pop() * cur_num)
                elif cur_ops == '/':
                    dividend = stack.pop()
                    tmp_res = -(-dividend // cur_num) if dividend < 0 else dividend // cur_num
                    stack.append(tmp_res)
                
                cur_num = 0
                cur_ops = cur_char
        
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
