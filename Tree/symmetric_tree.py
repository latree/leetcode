from Data_Structure.tree_node import TreeNode

class SymmetricTree:
    def isSymmetric(self, root: TreeNode) -> bool:
        # # solution 1: recursive
        # # time: O(n) number of n nodes in tree
        # # space: O(n) number of n nodes in tree
        # # 两个treeNode 是复制同一个tree 变成两份，然后同一个tree 镜面的traverse
        # def helper(t1: TreeNode, t2: TreeNode) -> bool:
        #     if not t1 and not t2:
        #         return True
        #     if not t1 or not t2:
        #         return False
        
        #     l = helper(t1.left, t2.right)
        #     r = helper(t1.right, t2.left)

        #     return l and r and (t1.val == t2.val)
    
        # return helper(root, root)

        # solution 2: iteration
        # time: O(n) number of n nodes in tree
        # space: O(n) number of n nodes in tree
        t1, t2 = root, root
        stack = [(t1, t2)]

        while stack:
            t1, t2 = stack.pop()
            if not t1 and not t2:
                # 这里不能直接return， 因为如果return true 那么最底部的node，都是（N，N），所以永远会return True
                continue
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            # if not t1_res or t2_res
            stack.append((t1.left, t2.right))
            stack.append((t1.right, t2.left))
        
        return True

    def call_function(self) -> None:

        root = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(4)))

        print(self.isSymmetric(root))