from typing import Optional
from Data_Structure.tree_node import TreeNode

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 我把这道题想复杂了，这就是单纯的flatten tree
        # 没有左子树大小的问题。
        # 只需要把左子树的最后一个node 连到右子树的第一个node，然后
        # 把整个左子树再移到右边
        def dfs(node):
            if not node:
                return 
            
            if not node.left and not node.right:
                return node
            
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            
            return right_tail if right_tail else left_tail
    
        dfs(root)