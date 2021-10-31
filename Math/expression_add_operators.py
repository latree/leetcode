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


        # 第二遍
        # recursion的解法可以做到以下就想出来，尤其是画出了recursion的tree。
        # 但是0的情况需要分情况讨论
        operations = ["+", "-", "*"]
        def evl(expr, target):
            if eval(expr) == target:
                return True
            return False
        
        
        def dfs(num, target, idx, cur_res, solutions):
            if idx == len(num):
                # need to check cur_res[-1] is digit???
                if cur_res[-1].isdigit() and evl(cur_res, target):
                    solutions.append(cur_res)
                return
            
            if cur_res == "":
                dfs(num, target, idx+ 1, cur_res + str(num[idx]), solutions)
            else:
                if cur_res[-1].isdigit():
                    if cur_res[-1] == "0":
                        n = len(cur_res)
                        # 只有以下条件的时候就是leading 0的情况。
                        # 也就是0 前面一位是运算符，不是数字。这种情况后面只能跟运算符，不能跟数字了
                        if n < 2 or (n >= 2 and not cur_res[n - 2].isdigit()):
                            for operates in operations:
                                dfs(num, target, idx, cur_res + operates, solutions)
                        else:
                            dfs(num, target, idx + 1, cur_res + num[idx], solutions)
                            for operates in operations:
                                dfs(num, target, idx, cur_res + operates, solutions)
                        
                    else:
                        dfs(num, target, idx + 1, cur_res + num[idx], solutions)
                        for operates in operations:
                            dfs(num, target, idx, cur_res + operates, solutions)
                
                else:
                    dfs(num, target, idx+ 1, cur_res + str(num[idx]), solutions)
        
        solutions = []
        dfs(num, target, 0, "", solutions)
        return solutions
        
        
        
        
        
  #                                               1
  #           1+2                       1*2                     1-2             12                  
  # 1+2+3 1+2-3 1+2*3             ...



    def call_function(self):
        self.addOperators("105", 5)
