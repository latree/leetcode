class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # [[a, 1], [b, 1]]
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append([s[i], 1])
            elif stack[-1][0] != s[i]:
                stack.append([s[i], 1])
            elif stack[-1][0] == s[i]:
                if stack[-1][1] == k - 1:
                    for _ in range(k - 1):
                        stack.pop()
                else:
                    count = stack[-1][1]
                    stack.append([s[i], count + 1])
        
        return "".join([i for i, v in stack])