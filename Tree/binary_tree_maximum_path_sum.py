from Data_Structure.tree_node import TreeNode
from typing import Optional
import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time:O(n)
        # space:O(n) n is tree height
        # 三个关键点，第一个这道题如果child subtree return回来是负数，那么我们可以直接忽略掉，因为负数加上一个当前的root node 
        # 不会比当前root node 大。
        # 第二个关键点是我们需要用一个res_max 一直记录到目前为止的一个最大sum是多少。
        # 第三个关键点是最后的return 不是return node.val + left_max + right_max, 是return 
        # node.val + max(left_max, right_max)。因为return 是一个单线的path，不是include所有child 的path线路
        def dfs(node):
            nonlocal res_max
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            cur_max = node.val + left_max + right_max
            res_max = max(res_max, cur_max)
            return node.val + max(left_max, right_max)

        res_max = -math.inf
        dfs(root)
        return res_max