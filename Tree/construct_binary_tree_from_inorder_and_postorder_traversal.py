from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:
    # https://mp.weixin.qq.com/s/OlpaDhPDTJlQ5MJ8tsARlA
    # 画边界的时候一定要把indorder_idx he inorder_idx - 1 画的清楚，这样在计算postorder 的left tree size的时候才不容易把idx 弄混
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder: List[int], in_start: int, in_end: int, 
                 postorder: List[int], post_start: int, post_end: int) -> Optional[TreeNode]:
            if in_start > in_end:
                return
            
            root_val = postorder[post_end]
            idx = inorder.index(root_val)
            
            root = TreeNode(root_val)
            left_size = idx - in_start
            
            root.left = build(inorder, in_start, idx - 1, postorder, post_start, post_start + left_size - 1)
            root.right = build(inorder, idx + 1, in_end, postorder, post_start + left_size, post_end - 1)
            return root
        
        
        return build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)