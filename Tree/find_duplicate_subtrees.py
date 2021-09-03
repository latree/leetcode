from Data_Structure.tree_node import TreeNode
from typing import Optional, List

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # 用set是不行的，因为如果使用set 那么每次重复都会加入到res 里面。
        # 多余重复的子树我们只需要一个，所以要不把res在开始的时候设立成set，要不
        # 在check的过程中我们必须保证重复多次的话，不会append到res 的list里面
        visited_subtree = {}
        res = []
        def get_subtree(root: Optional[TreeNode]) -> str:
            if not root:
                return "#"
            
            left = get_subtree(root.left)
            right = get_subtree(root.right)

            subtree = left + "," + right + "," + str(root.val)

            if visited_subtree.get(subtree, 0) == 1:
                res.append(root)

            visited_subtree[subtree] = visited_subtree.get(subtree, 0) + 1

            return subtree
        
        get_subtree(root)
        return res