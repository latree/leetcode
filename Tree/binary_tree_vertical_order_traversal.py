from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 一个没有想到的点是在于最后的结果是要按照矩阵的顺序打印出来。
        # 每一个treenode 都是有对应的矩阵的row，col 的idx的。我开始忽略了col的idx
        # Time: O(w) + 2*nlogn) 用了两次sorting. w是node 数量，n是每一个col node 数量
        # space: O(2*n) extra的space 去存结果
        def dfs(node, row, col, solutions):
            if not node:
                return
            if col not in solutions:
                solutions[col] = [(row, node.val)]
            else:
                solutions[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1, solutions)
            dfs(node.right, row + 1, col + 1, solutions)

        row, col = 0, 0
        solutions = {}
        dfs(root, row, col, solutions)
        tmp_keys = list(solutions.keys())
        tmp_keys.sort()
        res = []
        for key in tmp_keys:
            solutions[key].sort(key = lambda x: x[0])
            res.append([i for _, i in solutions[key]])
        return res