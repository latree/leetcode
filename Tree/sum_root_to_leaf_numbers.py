from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = [0]
        self.get_numbers(root, sums, 0)
        return sums[0]
        
    def get_numbers(self, root: Optional[TreeNode], sums:List[int], sum: int) -> None:
        if not root:
            return
        if not root.left and not root.right:
            sums[0] += sum * 10 + root.val
            return
        
        cur_sum = sum * 10 + root.val
        
        self.get_numbers(root.left, sums, cur_sum)
        self.get_numbers(root.right, sums, cur_sum)
        