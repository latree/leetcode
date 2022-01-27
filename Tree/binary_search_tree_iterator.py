from Data_Structure.tree_node import TreeNode
from typing import Optional

class BSTIterator:

# 第二遍：
# 最开始的想法是iterate整个tree 然后存在list里面，那个方法不对！！！！
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        temp = node.right
        
        while temp:
            self.stack.append(temp)
            temp = temp.left
        
        return node.val


    def hasNext(self) -> bool:

        return len(self.stack) > 0