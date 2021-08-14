from Data_Structure.tree_node import TreeNode
from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.sorted_node = []
        self.idx = -1
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.sorted_node.append(root)
        self._inorder(root.right)

    def next(self) -> int:
        self.idx += 1
        return self.sorted_node[self.idx].val


    def hasNext(self) -> bool:
        next_idx = self.idx + 1
        return next_idx < len(self.sorted_node)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()