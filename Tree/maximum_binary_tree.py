from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return
            
            temp_max = max(nums)
            temp_idx = nums.index(temp_max)
            
            root = TreeNode(temp_max)
            root.left = helper(nums[:temp_idx])
            root.right = helper(nums[temp_idx + 1:])
            return root
        
        return helper(nums)