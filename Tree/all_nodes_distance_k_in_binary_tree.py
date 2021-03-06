from Data_Structure.tree_node import TreeNode
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # res = []
        # # 用return 的value 表示distance from node to target, 如果target node 在左边，那么如果要move 到node.right 那么distance就要
        # # l + 1， 右边也是同理
        # def dfs(node):
        #     if not node:
        #         return -1
        #     elif node is target:
        #         subtree_add(node, 0)
        #         return 1
        #     else:
        #         l, r = dfs(node.left), dfs(node.right)
        #         if l != -1:
        #             if l == k: res.append(node.val)
        #             subtree_add(node.right, l + 1)
        #             return l + 1
        #         elif r != -1:
        #             if r == k: res.append(node.val)
        #             subtree_add(node.left, r + 1)
        #             return r + 1
        #         else:
        #             return -1

        # # 找到在subtree里面所有符合dist == k的node
        # def subtree_add(node, dist):
        #     if not node:
        #         return 
        #     elif dist == k:
        #         res.append(node.val)
        #     else:
        #         subtree_add(node.left, dist + 1)
        #         subtree_add(node.right, dist + 1)
        
        # dfs(root)
        # return res

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
    


# 第三遍：
        # 这道题一共分2个case
        #     case1：从target 下面的substree找到dist ==k的node，也就是if node == target: 这里表述的case。
        #     case2: case2.a 是target在当前node的分枝中。如果target在左分枝，那么我们就要到**右**分支找到k-left+1 的node，也是距离target是k的node
        #            case2.b 如果target在右分枝，那么我们就要到**左**分支找到k-right+1 的node，也是距离target是k的node
        #            case2.c 并且在case2 中还有一种情况就是，node自己本身就是到target 等于k距离的node，那么也要加进去
        def dfs(node, res, k):
            if not node:
                return -1
            
            # case1:
            if node == target:
                find_nodes(node, res, k)
                # 为什么这里return 1？ 是因为是一个bottom up 的过程。想象一下如果你站在target node的parent 位置，你应该得到
                # 结果就是target在我（parent node）的分枝，距离我为1的分枝里。
                return 1
            
            left = dfs(node.left, res, k)
            right = dfs(node.right, res, k)
            
            # case2:
            if left != -1:
                # case2.c
                if left == k:
                    res.append(node.val)
                # case2.a
                find_nodes(node.right, res, k - left - 1)
                return left + 1
            if right != -1:
                # case2.c
                if right == k:
                    res.append(node.val)
                # case2.b
                find_nodes(node.left, res, k - right - 1)
                return right + 1
            
            return -1
                    
            
        
        
        
        def find_nodes(node, res, dist):
            if not node:
                return
            if dist == 0:
                res.append(node.val)

            find_nodes(node.left, res, dist - 1)
            find_nodes(node.right, res, dist - 1)
        
        
        res = []
        dfs(root, res, k)
        return res

    def call_function(self) -> None:
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        self.distanceK(root, root.left, 2)




