from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # # Time:O(n**5) n**4 * n, n**4 is dfs, every position in str we have 4 choices +,-,*,next_digit
        #     #    another n is evalutation expression
        # # Space: O(n**4)
        # # 有一个corner case比较不好想到的就是0不能够成为一个数的开头。如果0前面没有数字，那么0后面只能跟运算符
        # # 如果0前面有数字，那么就可以即跟运算符也能跟数字
        # operations = ['+', '-', '*']
        # def evaluate(expr, target):
        #     if eval(expr) == target:
        #         return True
        #     return False

        # def dfs(num, idx, target, cur_res, solutions):
        #     if idx == len(num):
        #         if cur_res[-1].isdigit() and evaluate(cur_res, target):
        #                 solutions.append(cur_res)
        #         return
        #     if cur_res == "":
        #         dfs(num, idx + 1, target, cur_res + num[idx], solutions)
        #     else:
        #         if cur_res[-1].isdigit():
                    
        #             if cur_res[-1] == '0':
        #                 n = len(cur_res)
        #                 if n < 2 or (n >= 2 and not cur_res[n - 2].isdigit()):
        #                     for operator in operations:
        #                         dfs(num, idx, target, cur_res + operator, solutions)   
        #                 else:
        #                     dfs(num, idx + 1, target, cur_res + num[idx], solutions)
        #                     for operator in operations:
        #                         dfs(num, idx, target, cur_res + operator, solutions)
        #             else:                        
        #                 dfs(num, idx + 1, target, cur_res + num[idx], solutions)
        #                 for operator in operations:
        #                     dfs(num, idx, target, cur_res + operator, solutions)
        #         else:
        #             dfs(num, idx + 1, target, cur_res + num[idx], solutions)


        # solutions = []
        # dfs(num, 0, target, "", solutions)
        # return solutions


        # # 第二遍
        # # recursion的解法可以做到以下就想出来，尤其是画出了recursion的tree。
        # # 但是0的情况需要分情况讨论
        # operations = ["+", "-", "*"]
        # def evl(expr, target):
        #     if eval(expr) == target:
        #         return True
        #     return False
        
        
        # def dfs(num, target, idx, cur_res, solutions):
        #     if idx == len(num):
        #         # need to check cur_res[-1] is digit???
        #         if cur_res[-1].isdigit() and evl(cur_res, target):
        #             solutions.append(cur_res)
        #         return
            
        #     if cur_res == "":
        #         dfs(num, target, idx+ 1, cur_res + str(num[idx]), solutions)
        #     else:
        #         if cur_res[-1].isdigit():
        #             if cur_res[-1] == "0":
        #                 n = len(cur_res)
        #                 # 只有以下条件的时候就是leading 0的情况。
        #                 # 也就是0 前面一位是运算符，不是数字。这种情况后面只能跟运算符，不能跟数字了
        #                 if n < 2 or (n >= 2 and not cur_res[n - 2].isdigit()):
        #                     for operates in operations:
        #                         dfs(num, target, idx, cur_res + operates, solutions)
        #                 else:
        #                     dfs(num, target, idx + 1, cur_res + num[idx], solutions)
        #                     for operates in operations:
        #                         dfs(num, target, idx, cur_res + operates, solutions)
                        
        #             else:
        #                 dfs(num, target, idx + 1, cur_res + num[idx], solutions)
        #                 for operates in operations:
        #                     dfs(num, target, idx, cur_res + operates, solutions)
                
        #         else:
        #             dfs(num, target, idx+ 1, cur_res + str(num[idx]), solutions)
        
        # solutions = []
        # dfs(num, target, 0, "", solutions)
        # return solutions
        
        # 第三遍
        # 这道题最开始的方法已经过不了test了。
        # 这个方法理解起来比较直接。
        # 在组成cur_expr的每一个idx都有四个分枝， 那就是 ["+", "-", "*", ""]. 所以recursion tree 就比较简单明了了。
        # 接下来就是砍枝的过程。
        def dfs(idx, num, target, cur_expr, exprs, ops):
            # 如果cur_expr 里只有一个char 而且是0， 那么就是leading 0。 所以直接return，砍掉。 ---> 原因是 剩余的三个分枝已经cover了所有情况，也就是 cur_expr + x  lambda x: in ["0+", "0-", "0*"]. 、

            if len(cur_expr) == 1 and cur_expr[-1] == "0":
                return
            # 同理如果遇到这样的leading 0， 那么也要砍枝砍掉
            if len(cur_expr) >= 2 and cur_expr[-2:] in ["+0", "-0", "*0"]:
                return
            
            # 这里也要注意， 因为我们每一次加元素到cur_expr 是加 + num[idx] + op. 所以如果条件写成 idx >= len(num) 就会出现cur_expr[-1] 可能是符号的情况。
            # 所以必须要在idx 等于最后一个元素的时候，直接append 最后一个元素来check
            if idx == len(num) - 1:
                if eval(cur_expr + num[idx]) == target:
                    exprs.append(cur_expr + num[idx])
                return
            
            for op in ops:
                # 注意！！！！
                # 在recursion的过程中每一次都是加的  num[idx] + op
                dfs(idx + 1, num, target, cur_expr + num[idx] + op, exprs, ops)


        res = []
        ops = ["+", "-", "*", ""]
        dfs(0, num, target, "", res, ops)
        return res
        
        
        
  #                                               1
  #           1+2                       1*2                     1-2             12                  
  # 1+2+3 1+2-3 1+2*3             ...



    def call_function(self):
        self.addOperators("105", 5)
