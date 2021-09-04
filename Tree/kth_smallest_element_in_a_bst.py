from Data_Structure.tree_node import TreeNode
from typing import Optional, List
import math

class Solution:
    def __init__(self):
        self.res = math.inf
        self.cur = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root: Optional[TreeNode], k: int) -> None:            
            if not root:
                return
            helper(root.left, k)
            self.cur += 1
            if self.cur == k:
                self.res = root.val
                return
            helper(root.right, k)
            
        helper(root, k)
        return self.res