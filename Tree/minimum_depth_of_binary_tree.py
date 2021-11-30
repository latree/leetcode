from collections import deque
from typing import Optional
from Data_Structure.tree_node import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth 
        
        
        queue = deque()
        queue.append(root)
        
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        
        return depth
    