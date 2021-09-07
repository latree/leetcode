from Data_Structure.tree_node import TreeNode
from typing import Optional

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 最简单的判定方法就是用前后两个指针代表cur 和pre node， 一旦
        # pre 是none cur 不是none，那么就不是complete binary tree
        queue = deque()
        queue.append(root)
        
        pre_node = TreeNode(-1)
        cur_node = TreeNode(-1)
        while queue:
            cur_size = len(queue)
            for i in range(cur_size):
                pre_node = cur_node
                cur_node = queue.popleft()
                
                if not pre_node and cur_node:
                    return False
                
                if cur_node:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
                
        return True