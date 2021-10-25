class Solution:
    def removeDuplicates(self, s: str) -> str:
#         # 要充分理解一下adjacent 这个词，只能是看到第一个重复的时候remove，不是看到所有重复的以后再remove
#         stack = []
        
#         for ch in s:
#             if stack and ch == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(ch)
#         return "".join(stack)


# # Input: s = "abbaca"
# # Output: "ca"

# # a b  b  b  a c a 
# #              i


# # stack = [c]

        # 第二遍
        dup_stack = []
        for i in range(len(s)):
            if dup_stack:
                if s[i] == dup_stack[-1]:
                    dup_stack.pop()
                else:
                    dup_stack.append(s[i])
            else:
                dup_stack.append(s[i])
        
        return "".join(dup_stack)