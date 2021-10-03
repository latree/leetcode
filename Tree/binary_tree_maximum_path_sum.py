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
            # 因为有负数的情况, 所以要让左右先变成非负数
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # 因为是寻找最大的path，如果用top down 做是找不到的，因为都没有traverse 到所有的node 
            # 如何知道最大的path？
            cur_max = node.val + left_max + right_max
            res_max = max(res_max, cur_max)
            return node.val + max(left_max, right_max)

        res_max = -math.inf
        dfs(root)
        return res_max