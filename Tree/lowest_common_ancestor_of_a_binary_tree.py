from Data_Structure.tree_node import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 刚开始没有想清楚如果保存这个lowestCommonAncestor
        # res = None
        # def dfs(node: TreeNode) -> bool:
        #     nonlocal res
        #     if not node:
        #         return False
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     mid = node == p or node == q

        #     if mid + left + right >= 2:
        #         res = node
        #     return mid or left or right
        
        # dfs(root)
        # return res

    # 第二遍：
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        if not left and not right:
            return None
        
        if not left and right:
            return right
        
        if left and not right:
            return left