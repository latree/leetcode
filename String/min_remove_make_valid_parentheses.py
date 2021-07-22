

class minRemoveToMakeValid:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Time: O(2n)
        # Space: O(4n) 
        # open parentheses index
        open = []
        # close parentheses index
        close = []
        # delete at the beginning
        to_del = []

        for i in range(len(s)):
            if s[i] == '(':
                open.append(i)
            elif s[i] == ')':
                if not open:
                    to_del.append(i)
                else:
                    open.pop()
        
        final_del = set(open + close + to_del)

        res = ''
        for i in range(len(s)):
            if i not in final_del:
                res += s[i]
        
        return res