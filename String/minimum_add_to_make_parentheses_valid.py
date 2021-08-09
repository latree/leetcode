class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            else:
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        return len(stack)