from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Time:O(n**5) n**4 * n, n**4 is dfs, every position in str we have 4 choices +,-,*,next_digit
            #    another n is evalutation expression
        # Space: O(n**4)
        # 有一个corner case比较不好想到的就是0不能够成为一个数的开头。如果0前面没有数字，那么0后面只能跟运算符
        # 如果0前面有数字，那么就可以即跟运算符也能跟数字
        operations = ['+', '-', '*']
        def evaluate(expr, target):
            if eval(expr) == target:
                return True
            return False

        def dfs(num, idx, target, cur_res, solutions):
            if idx == len(num):
                if cur_res[-1].isdigit() and evaluate(cur_res, target):
                        solutions.append(cur_res)
                return
            if cur_res == "":
                dfs(num, idx + 1, target, cur_res + num[idx], solutions)
            else:
                if cur_res[-1].isdigit():
                    
                    if cur_res[-1] == '0':
                        n = len(cur_res)
                        if n < 2 or (n >= 2 and not cur_res[n - 2].isdigit()):
                            for operator in operations:
                                dfs(num, idx, target, cur_res + operator, solutions)   
                        else:
                            dfs(num, idx + 1, target, cur_res + num[idx], solutions)
                            for operator in operations:
                                dfs(num, idx, target, cur_res + operator, solutions)
                    else:                        
                        dfs(num, idx + 1, target, cur_res + num[idx], solutions)
                        for operator in operations:
                            dfs(num, idx, target, cur_res + operator, solutions)
                else:
                    dfs(num, idx + 1, target, cur_res + num[idx], solutions)


        solutions = []
        dfs(num, 0, target, "", solutions)
        return solutions

    def call_function(self):
        self.addOperators("105", 5)
