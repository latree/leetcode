from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root