class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class treeToDoublyList:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # Time:O(n) number of nodes
        # Space: O(n) best case logn which is height of tree. n is worst case. tree is a list
        # inorder traversal 在BST 的本质就是 以从小到大的顺序浏览整个的tree。 如果想象这个过程其实就是跟从头到尾浏览
        # double linked list 是一样的。 只需要记住第一个和最后一个node 是什么，好让当前的node 和最后一个node 相连接就可以了
        # 第一个node 只起到一个作用就是在最后的时候和最后一个node 连接形成闭环
        def helper(root: 'Node') -> 'Node':
            nonlocal first, last
            if not root:
                return None
            helper(root.left)
            if last:
                last.right = root
                root.left = last
            else:
                first = root
            last = root
            helper(root.right)

        if not root:
            return None
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first