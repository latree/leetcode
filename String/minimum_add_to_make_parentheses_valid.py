class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # # Time: O(n)
        # # Space: O(n)
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append('(')
        #     else:
        #         if stack:
        #             if stack[-1] == '(':
        #                 stack.pop()
        #             else:
        #                 stack.append(s[i])
        #         else:
        #             stack.append(s[i])
        # return len(stack)
    

    # 第二遍：
        # 这里没有用到stack，但是其实是用到了stack的概念。
        open_c = 0
        close_c = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_c += 1
            elif s[i] == ")":
                if open_c > 0:
                    open_c -= 1
                else:
                    close_c += 1
        
        return open_c + close_c