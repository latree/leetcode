class validParentheses:
    def isValid(self, s: str) -> bool:
        # solution 1: stack
        stack = []
        valid_map = {')': '(', ']': '[', '}': '{'}
        i, j = 0, 0

        while i < len(s):
            if not stack or s[i] not in valid_map or valid_map[s[i]] != stack[-1]:
                stack.append(s[i])
                i += 1
                continue
            stack.pop()
            i += 1
    
        return True if not stack else False
    
    def call_function(self) -> None:
        self.isValid("([)]")