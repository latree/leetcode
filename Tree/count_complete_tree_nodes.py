from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left, right = root, root
        hl, hr = 0,0
        
        while left:
            left = left.left
            hl += 1
        
        while right:
            right = right.right
            hr += 1
        
        if hl == hr:
            return 2**hr - 1
        # 不需要这一部分的代码，如果是叶节点，那么return 2**hr - 1 就会return 0.
        # if not root:
        #     return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)