from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # def dfs(node: TreeNode) -> List:
        #     if node:
        #         return dfs(node.left) + [node.val] + dfs(node.right)
        #     else:
        #         return []
        
        # return min(dfs(root), key= lambda x: abs(target - x))
        
        # solution 2:
        closet = root.val
        while root:
            closet = min(root.val, closet, key= lambda x: abs(target - x))
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closet
