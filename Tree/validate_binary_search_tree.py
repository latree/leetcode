import math
from typing import List

from Data_Structure.tree_node import TreeNode

class ValidBST:
    def isValidBST(self, root: TreeNode) -> bool:
        # 这是记忆当中的做法
        # 可以想象一下：如果把BST看招中序遍历打印出来的时候那么肯定是
        # [low....root.val....high]
        # 那么问题就在于如果设定左边界和右边界。在第一层进入的时候你只知道root并不知道左右边界的边界值是什么。
        # 只有在进入第一层root.left 的时候你才知道你的left部分的右边界就是root.val
        # 同理 只有在进入第一层root.right 的时候你才知道你的right部分的左边界就是root.val
        # 一个比较容易想错的case 在这篇文章里有提到
        # https://labuladong.gitee.io/algo/2/19/25/
            #        10
            #     /         \
            # 5               15
            #                /
            #             6
            
        # 显然 6 不能出现在15的左子树里

        # # solution 1: straight forward recursion  
        # # time:O(n) n should be the total number of tree nodes. 
        # # space: avg: O(2**math.log2(n-1)) n is the total number of nodes. O(2**math.log2(n-1)) stands for max
        # # number of nodes in one layer. The max spce complexity would be O(n) n is number of nodes.
        # max_int = math.inf
        # min_int = -math.inf
        # def helper(root: TreeNode, low: int, high: int) -> bool:            
        #     if not root:
        #         return True
        #     # 不管是bottom up 还是top down 其实都是一样的
        #     # return left and right and (low < root.val< high)

        #     if not (low < root.val< high):
        #         return False
            
        #     left = helper(root.left, low, root.val)
        #     right = helper(root.right, root.val, high)
            

        #     return left and right
        
        # return helper(root, min_int, max_int)
        
        # # solution 2: BFS
        # # time: O(n) number of nodes
        # # space: O(n) number of nodes
        # if not root:
        #     return True
        
        # stack = [(root, -math.inf, math.inf)]

        # while stack:
        #     node, low, high = stack.pop()
        #     if not node:
        #         continue
        #     if not (low < node.val < high):
        #         return False
            
        #     stack.append((node.left, low, node.val))
        #     stack.append((node.right, node.val, high))
    
        # return True

        # # solution 3: inorder traversal
        # # time: O(n)
        # # space:O(n)
        # def helper(root: TreeNode) -> bool:

        #     if not root:
        #         return True
            
        #     l = helper(root.left)
        #     if root.val <= self.prev:
        #         return False
        #     self.prev = root.val
        #     r = helper(root.right)

        #     return l and r
        
        # self.prev = -math.inf
        # return helper(root)
        
        # solution 4: stack by using iteration inorder traversal
        # time: O(n)
        # space: O(n)
        if not root:
            return True
        
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        
        return True 


    def call_function(self) -> None:
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

        print(self.isValidBST(root))