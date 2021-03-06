from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 这道题我们的答题思路是有的，但是没有想到用一个简单的int 来代替stack的作用。
        # 还有吧数min_remove_count 的过程复杂化了。非得用一个open 和一个close var 代表
        # Time:O(2**n)
        # Space: O(n)
        N = len(s)

        def find_l_r_count():
            open_p, min_remove_count = 0, 0
            for i in range(N):
                if s[i] == '(':
                    open_p += 1
                elif s[i] == ')':
                    if open_p > 0:
                        open_p -= 1
                    else:
                        min_remove_count += 1
            return min_remove_count + open_p

        def dfs(s, min_remove_count, idx, solutions, cur_solution, open_p):
            if idx == N:
                # 这里有可能miss 掉 open_p ==0 因为我们必须保证最后的solution是valid solution的话
                #open 这个integer其实是非常简化版的stack 可以帮助我们判断。
                if min_remove_count == 0 and open_p == 0:
                    solutions.add(cur_solution)
                return
            if min_remove_count < 0:
                return

            if s[idx] == '(':
                # no deletion
                dfs(s, min_remove_count, idx + 1, solutions, cur_solution+s[idx], open_p + 1)
                # delete the cur open
                dfs(s, min_remove_count - 1, idx + 1, solutions, cur_solution, open_p)

            elif s[idx] == ')':
                if open_p > 0 :
                    # no deletion
                    dfs(s, min_remove_count, idx + 1, solutions, cur_solution+s[idx], open_p - 1)
                # delete the cur close
                dfs(s, min_remove_count - 1, idx + 1, solutions, cur_solution, open_p)

            else:
                dfs(s, min_remove_count, idx + 1, solutions, cur_solution+s[idx], open_p)
        
        min_remove_count = find_l_r_count()
        solutions, cur_solution = set([]), ""
        dfs(s, min_remove_count, 0, solutions, cur_solution, 0)
        return list(solutions)

    def call_function(self) -> None:
        self.removeInvalidParentheses("")

# "(a)())()"
# (  (  (  (  )   (   )   ) 
#   0  1  2  3  4   5   6   7
 

# 1                            root    
# 2                   (                           ""
# 3               (a                              a
# 4       (a)          (a(                 a)                a(
# 5   (a)(  (a))    ...   ...         ...     ...       ...      ....


# 第二遍心得：
        # *************** notes ***************
        # 1. remove min number of params, 就是到i为止多余出来的关括号加上之后又多出来的开括号
        # 最简单的例子就是 Input: s = ")("
        # 2. 对于开关括号的题基本就是用dfs 来做，然后tree 的样子就是每一个idx上删除和不删除当前这个括号
        # 对于开括号怎么删，关括号怎么删要具体讨论
        def get_min_count(s):
            min_count, open_p = 0, 0
            for i in range(len(s)):
                if s[i] == "(":
                    open_p += 1
                elif s[i] == ")":
                    if open_p > 0:
                        open_p -= 1
                    else:
                        min_count += 1
            return min_count + open_p
                        
        def dfs(s, idx, min_count, open_p, res, cur_res):
            if idx == len(s):
                if min_count == 0 and open_p == 0:
                    res.add(cur_res)
                return
            
            if s[idx] == "(":
                # no deletion
                dfs(s, idx + 1, min_count, open_p + 1, res, cur_res + s[idx])
                # deletion
                dfs(s, idx + 1, min_count - 1, open_p, res, cur_res)
            elif s[idx] == ")":

                # *************** notes ***************
                # 这里必须有这个条件才能做关括号的no deletion。因为如果没有这个条件，那么
                # no deletion 就会让open_p -1 那么如果已经没有open_p，就会导致出现负数
                if open_p > 0:                    
                    # no deletion
                    dfs(s, idx + 1, min_count, open_p - 1, res, cur_res + s[idx])
                
                # deletion
                dfs(s, idx + 1, min_count - 1, open_p, res, cur_res)
            else:
                dfs(s, idx + 1, min_count, open_p, res, cur_res + s[idx])
                
        min_count = get_min_count(s)
        res = set()
        dfs(s, 0, min_count, 0, res, "")
        return res