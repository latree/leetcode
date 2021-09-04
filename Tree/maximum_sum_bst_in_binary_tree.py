from Data_Structure.tree_node import TreeNode
from typing import Optional, List
import math
class Solution:
    def __init__(self):
        self.max_sum = 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # 这道题如果用top down的方法在每一个节点都要有另外的三个recursion function去计算
        # res[1], res[2], res[3]. 这样每个节点都有3个recursion嵌套的的复杂度会非常大
        # 如果是用bottom up，那么随着bottom up的过程，把这些值记录下来一层一层投往上推那么
        # 那么就会省去嵌套的recursion
        def traverse(root: Optional[TreeNode]) -> List[int]:
            # base condition
            if not root:
                return [1, math.inf, -math.inf, 0]
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            res = [0] * 4
            # res[0] 记录以 root 为根的二叉树是否是 BST，若为 1 则说明是 BST，若为 0 则说明不是 BST；
            # res[1] 记录以 root 为根的二叉树所有节点中的最小值；
            # res[2] 记录以 root 为根的二叉树所有节点中的最大值；
            # res[3] 记录以 root 为根的二叉树所有节点值之和。
            if left[0] == 1 and right[0] == 1 and root.val > left[2] and root.val < right[1]:
                res[0] = 1
                res[1] = min(left[1], root.val)
                res[2] = max(right[2], root.val)
                res[3] = left[3] + right[3] + root.val
                
                self.max_sum = max(res[3], self.max_sum)
            else:
                res[0] = 0
            return res
        
        traverse(root)
        return self.max_sum
                