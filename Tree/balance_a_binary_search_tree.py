from Data_Structure.tree_node import TreeNode
from typing import Optional, List
class Solution:
    # 刚开始把这道题想复杂了，想到进入每一个节点如何去balance 这个node，那case 就非常多了。
    # 其实只要得到所有的node list，然后重新construct 出来一个bst就可以了
    # 因为是inorder 打印，所以values 是单调递增，那么construct 找mid 方式也是binary search 的方式
    # 那么就可以保证左子树和右子树都是balance 的情况。
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        self.inorder(root, values)
        node = self.construct_bst(values)
        return node
    
    
    def inorder(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return
        
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)
        
    
    def construct_bst(self, values: List[int]) -> TreeNode:
        if not values:
            return
        
        l, r = 0, len(values) - 1
        
        mid = l + (r - l) // 2
        root = TreeNode(values[mid])
        
        root.left = self.construct_bst(values[0: mid])
        root.right = self.construct_bst(values[mid + 1:])
        return root