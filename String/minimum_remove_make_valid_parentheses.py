

class minRemoveToMakeValid:
    def minRemoveToMakeValid(self, s: str) -> str:
        # # Time: O(2n)
        # # Space: O(4n) 
        # # open parentheses index
        # open = []
        # # close parentheses index
        # close = []
        # # delete at the beginning
        # to_del = []

        # for i in range(len(s)):
        #     if s[i] == '(':
        #         open.append(i)
        #     elif s[i] == ')':
        #         if not open:
        #             to_del.append(i)
        #         else:
        #             open.pop()
        
        # final_del = set(open + close + to_del)

        # res = ''
        # for i in range(len(s)):
        #     if i not in final_del:
        #         res += s[i]
        
        # return res

# 第二遍
        # 用open 来记录open 和close 的配对情况，也就是记录需要delete的open的idx
        # 用to_del 来记录需要delete的close 的括号的idx
        open_c = []
        to_del = []
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                open_c.append(i)
            elif s[i] == ")":
                if open_c:
                    open_c.pop()
                else:
                    to_del.append(i)
        
        final_del = set(open_c + to_del)
        
        for i in range(len(s)):
            if i not in final_del:
                res += s[i]
        return res