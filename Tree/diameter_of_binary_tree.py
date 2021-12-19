from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # # Time:O(n)
        # # Space:O(n) n height of tree
        # # 用一个global value 去记录最大的diameter
        # # 更新diameter的时候是left_diameter + right diameter 与 之前最大的diameter 比较
        # diameter = 0
        # def dfs(node: TreeNode) -> int:
        #     nonlocal diameter

        #     if not node:
        #         return 0

        #     left_diameter = dfs(node.left)
        #     right_diameter = dfs(node.right)

        #     diameter = max(diameter, left_diameter + right_diameter)
        #     cur_path = 1 + max(left_diameter, right_diameter)
        #     return cur_path

        # dfs(root)
        # return diameter


        # 第二遍        
        def dfs(node, diameter):
            if not node:
                return 0

            left = dfs(node.left, diameter)
            right = dfs(node.right, diameter)
            
            # 这里在第二次的时候写成了 diameter[0] = max(diameter[0], left + 1 + right)
            # 如果写成上面这样其实是相当于在count左边加右边加中间node的node的个数。
            # 如果想计算path的长度的话其实就不用加1 直接写成left + right 就可以了
            diameter[0] = max(diameter[0], left +  right)
            return max(left, right) + 1
        
        res = [0]
        dfs(root, res)
        return res[0]