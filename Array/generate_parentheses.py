class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, l, r, cur_res, final_res):
            if len(cur_res) == n * 2:
                final_res.append(cur_res)
                return
            # if r > l:
            #     return
            if l < n:
                dfs(n, l + 1, r, cur_res + '(', final_res)
            
            if r < l:
                dfs(n, l, r + 1, cur_res + ')', final_res)
            
        res = []
        dfs(n, 0, 0, "", res)
        return res

# n= 3
#                                   (
#                      ()                                  ((
#                     ()(                         (((                    (()
#             ()()        ()((                    ((()           (())        (()(                        
#             ()()(       ()(()                   ((())          (())(       (()()
#             ()()()      ()(())                  ((()))         (())()      (()())
                                         