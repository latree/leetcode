from Data_Structure.tree_node import TreeNode
from typing import Optional, List
class Solution:
    # The solution is well explained
    # https://mp.weixin.qq.com/s/OlpaDhPDTJlQ5MJ8tsARlA
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder: List[int], pre_start: int, pre_end: int, 
                 inorder: List[int], in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return
            
            root_val = preorder[pre_start]
            idx = inorder.index(root_val)
            
            root = TreeNode(root_val)
            left_size = idx - in_start
            
            root.left = build(preorder, pre_start + 1, pre_start + left_size, inorder, in_start, idx - 1)
            root.right = build(preorder, pre_start + left_size + 1, pre_end, inorder, idx + 1, in_end)
            return root
        
        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)