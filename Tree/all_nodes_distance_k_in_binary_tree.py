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

# #         这道题最主要的地方在于要把到target 的k 距离的node 分为两个部分
# #         第一部分：从target往下的子树里为k距离的node
# #         第二部分：跟target不在一个分枝里的target的parents 的分枝里 距离为k-x的距离
# #             这个x就是target 到那个parents的距离。也就是说如果target在左分枝，那么就从那个parent 开始算的
# #             k-left 的距离的nodes。如果target在右分枝，那么就从那个parent 开始算的
# #             k-right 的距离的nodes，
        
#         res = []
        
#         def dfs(node, res, k):
#             if not node:
#                 return 0
            
#             elif node == target:
#                 subtreeDistance(node, res, k)
#                 return 1
            
#             else:
#                 left = dfs(node.left, res, k)
#                 right = dfs(node.right, res, k)
#                 if left != 0:
#                     if left == k:
#                         res.append(node.val)
#                     # 如果是k-left 那么还要再减一，因为你从node 又走到了node.left也需要距离
#                     # 我第一个implementation 就没有这个问题。因为subtreeDistance 里的条件是反的
#                     subtreeDistance(node.right, res, k - left - 1)
#                     return left + 1

#                 elif right != 0:
#                     if right == k:
#                         res.append(node.val)
#                     subtreeDistance(node.left, res, k - right - 1)
#                     return right + 1
                    
#                 else:
#                     return 0
        
#         def subtreeDistance(root, res, dist):
#             if not root:
#                 return
#             if dist == 0:
#                 res.append(root.val)
#             subtreeDistance(root.left, res, dist - 1)
#             subtreeDistance(root.right, res, dist - 1)
    

    def call_function(self) -> None:
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        self.distanceK(root, root.left, 2)




