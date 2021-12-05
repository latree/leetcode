from Data_Structure.tree_node import TreeNode

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Time: O(n)
        # Space: O(n)
        # 最简单的写法就是不带if的traverse整个tree ，然后只要node.val 在range之内就加进去
        # 但是这样的话需要遍历整个tree
        # 优化的方法就是不去遍历那些不在range里面的node。所以要加上一些if condition去遍历tree node
        
        if not root:
            return 0
        res = 0

        if root.val < low:
            res += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            res += self.rangeSumBST(root.left, low, high)
        else:
            res += root.val
            res += self.rangeSumBST(root.left, low, high)
            res += self.rangeSumBST(root.right, low, high)

        return res