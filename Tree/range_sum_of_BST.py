from Data_Structure.tree_node import TreeNode

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Time: O(n)
        # Space: O(n)
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