from Data_Structure.tree_node import TreeNode
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        # 用return 的value 表示distance from node to target, 如果target node 在左边，那么如果要move 到node.right 那么distance就要
        # l + 1， 右边也是同理
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                l, r = dfs(node.left), dfs(node.right)
                if l != -1:
                    if l == k: res.append(node.val)
                    subtree_add(node.right, l + 1)
                    return l + 1
                elif r != -1:
                    if r == k: res.append(node.val)
                    subtree_add(node.left, r + 1)
                    return r + 1
                else:
                    return -1

        # 找到在subtree里面所有符合dist == k的node
        def subtree_add(node, dist):
            if not node:
                return 
            elif dist == k:
                res.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)
        
        dfs(root)
        return res


    

    def call_function(self) -> None:
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        self.distanceK(root, root.left, 2)




