from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time:O(n)
        # Space:O(n) n height of tree
        # 用一个global value 去记录最大的diameter
        # 更新diameter的时候是left_diameter + right diameter 与 之前最大的diameter 比较
        diameter = 0
        def dfs(node: TreeNode) -> int:
            nonlocal diameter

            if not node:
                return 0

            left_diameter = dfs(node.left)
            right_diameter = dfs(node.right)

            diameter = max(diameter, left_diameter + right_diameter)
            cur_path = 1 + max(left_diameter, right_diameter)
            return cur_path

        dfs(root)
        return diameter