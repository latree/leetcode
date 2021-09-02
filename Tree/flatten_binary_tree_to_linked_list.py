from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        
        p = root
        while p.right:
            p = p.right
            
        p.right = right
        
        