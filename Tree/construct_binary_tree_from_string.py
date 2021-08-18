from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # 这个题的每一步的步骤非常难定义。
        def get_number(s, idx):
            is_neg = False

            if s[idx] == '-':
                is_neg = True
                idx += 1
            
            num = 0
            while idx < len(s) and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1
            
            return (-num if is_neg else num, idx)

        if not s:
            return None
        root = TreeNode()
        stack = [root]
        idx = 0
        while idx < len(s):
            node = stack.pop()
            if s[idx].isdigit() or s[idx] == '-':
                value, idx = get_number(s, idx)
                node.val = value
                
                if idx < len(s) and s[idx] == '(':
                    stack.append(node)
                    node.left = TreeNode()
                    stack.append(node.left)
            elif idx < len(s) and s[idx] == '(':
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)
            idx += 1
        
        return stack.pop() if stack else root



# Input: s = "404 ( 2 ( 3 ) ( 1 ) ) ( 6 ( 5 ) )"
#                                             i
# # Output: [4,2,6,3,1,5]

# stack: [root(4), ]
# node: 

# set root.left.right = TreeNode()

#                     4
#             2               6 
#     3           1       5