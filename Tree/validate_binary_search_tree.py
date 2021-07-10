import math

from Data_Structure.tree_node import TreeNode

class ValidBST:
    def isValidBST(self, root: TreeNode) -> bool:
        # solution 1: straight forward recursion  
        max_int = math.inf
        min_int = -math.inf
        def helper(root: TreeNode, low: int, high: int) -> bool:            
            if not root:
                return True
            if not (low < root.val< high):
                return False
            
            left = helper(root.left, low, root.val)
            right = helper(root.right, root.val, high)
            

            return left and right 
        
        return helper(root, min_int, max_int)