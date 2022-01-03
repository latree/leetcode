from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
#         # 这个题的每一步的步骤非常难定义。
#         def get_number(s, idx):
#             is_neg = False

#             if s[idx] == '-':
#                 is_neg = True
#                 idx += 1
            
#             num = 0
#             while idx < len(s) and s[idx].isdigit():
#                 num = num * 10 + int(s[idx])
#                 idx += 1
            
#             return (-num if is_neg else num, idx)

#         if not s:
#             return None
#         root = TreeNode()
#         stack = [root]
#         idx = 0
#         # 如果遇到的是数字：
#         # 如果遇到的是开括号
#         #     数字后面直接跟开括号
#         #     数字后面不直接跟开括号
#         # 如果遇到的是关括号
#         while idx < len(s):
#             node = stack.pop()
#             if s[idx].isdigit() or s[idx] == '-':
#                 value, idx = get_number(s, idx)
#                 node.val = value
                
#                 if idx < len(s) and s[idx] == '(':
#                     stack.append(node)
#                     node.left = TreeNode()
#                     stack.append(node.left)
#             elif idx < len(s) and s[idx] == '(':
#                 stack.append(node)
#                 node.right = TreeNode()
#                 stack.append(node.right)
#             idx += 1
        
#         return stack.pop() if stack else root



# # Input: s = "404 ( 2 ( 3 ) ( 1 ) ) ( 6 ( 5 ) )"
# #                                             i
# # # Output: [4,2,6,3,1,5]

# # stack: [root(4), ]
# # node: 

# # set root.left.right = TreeNode()

# #                     4
# #             2               6 
# #     3           1       5


# 第二遍
#         这道题用recursion 做比较好理解。
#         第一：pre order create node
#         然后分别把左子树的sub-string 和右子树的sub-string pass 进node.left 和node.right recursion call
#         recursion的层数就是tree的层数，分差就是tree的分差。
#         第二：最关键的是找到左子树和右子树的sub-string ，然后分割substring，分别pass 进recursion call
        if not s:
            return None
        
        # ***** impartant ******
        # 如何找到左子树的substring 起始点和右子树的substring 起始点
        # 这里没有想到
        # define left is left node open param idx
        # define right is right node open param idx
        # 4(
        #     2(3)(1)
        # )
        # (
        #     6(5)
        # )
    
        left, right = len(s), len(s)
        open_param = 0
        
        for i, ch in enumerate(s):
            if ch == "(":
                open_param += 1
            if ch == ")":
                open_param -= 1
            if ch == "(" and open_param == 1:
                if left == len(s):
                    left = i
                else:
                    right = i
            
        
        node = TreeNode(int(s[:left]))
        node.left = self.str2tree(s[left + 1: right - 1])
        node.right = self.str2tree(s[right + 1:-1])
        return node