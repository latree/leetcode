from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 这道题很巧妙的地方在于我们用了从小到大的中序遍历。然后这个从小到大的顺序正好符合题意做累加
        # 那么每次遍历到的node 就需要把当前的sum 值加上自己的node val 是累加的值
        def get_sum_greater_tree(root: Optional[TreeNode]) -> None:
            if not root:
                return
            
            get_sum_greater_tree(root.right)
            self.sum += root.val
            root.val = self.sum
            get_sum_greater_tree(root.left)

        get_sum_greater_tree(root)
        return root
        
        