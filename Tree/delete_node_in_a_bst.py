from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_min(node: Optional[TreeNode]) -> TreeNode:
            while node.left:
                node = node.left
            return node
    
        if not root:
            return
        
        if root.val == key:
            # 两个if 包含了root 是leaf 的case 和root 只有一个子树的情况
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 这个case是root 两个子树都存在的情况
            min_node = get_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        
        return root
    
            