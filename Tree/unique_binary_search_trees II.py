from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def buildTree(low: int, high: int) -> List[Optional[TreeNode]]:
            res = []
            if low > high:
                return [None]
            
            for i in range(low, high + 1):
                left = buildTree(low, i - 1)
                right = buildTree(i + 1, high)
                for left_tree in left:
                    for right_tree in right:
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        res.append(root)
            return res
        
        return buildTree(1, n)