from typing import List
from Data_Structure.tree_node import TreeNode

class LevelOrder:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # # solution 1: iteration
        # if not root:
        #     return []

        # queue = [root]
        # res = []
        # while queue:
        #     layer = []
        #     queue_size = len(queue)
        #     for _ in range(queue_size):
        #         # popleft is good to know
        #         node = queue.popleft()
        #         layer.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(layer)

        # return res

        # solution 2: recursion
        layers = []
        if not root:
            return []
        def helper(root: TreeNode, level_idx: int, layers: List[list[int]]) -> None:
            # 这一步也非常关键而且巧妙，这个是用来判定进入下一层以后，layers里面是不是已经创建了这一层的list还是没有创建这一层的list
            # 这里还非常巧妙的运用到了 idx 和len 是相差1的。因为相差1，所以在他们相等的时候就说明我们进入了下一个level_idx,但是这一层的
            # list 并没有被创建
            if len(layers) == level_idx:
                layers.append([])
            
            # 其实这样和加上以下代码是一样的效果
            # if not root.left and not root.right:
            #     layers[level_idx].append(root.val)
            #     return
            # 如果当前node是leaf，那么在运行以下代码以后也没有后续的recursive call了。所以就会一直return bottom up 回去

            layers[level_idx].append(root.val)

            if root.left:
                helper(root.left, level_idx + 1, layers)
            if root.right:
                helper(root.right, level_idx + 1, layers)
                
        helper(root, 0, layers)
        return layers

    def call_function(self) -> None:

        root = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(4)))

        print(self.levelOrder(root))