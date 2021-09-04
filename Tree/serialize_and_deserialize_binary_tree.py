from Data_Structure.tree_node import TreeNode
from typing import Optional, List
import math

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # string 在python 里是immutable 的。所以不能直接pass in 成args 
        # 然后再recursion 的function里随意更改。如果需要这样的性质，并且最后要return 这个string，
        # 那么就可以用res[str]的方式做
        def helper(node: TreeNode, tree_str: List[str]) -> None:
            if not node:
                tree_str[0] += "#,"
                return

            tree_str[0] += str(node.val) + ","
            helper(node.left, tree_str)
            helper(node.right, tree_str)
            
        res = [""]
        helper(root, res)
        return res[0]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(nodes: List[str]) -> TreeNode:
            if not nodes:
                return
            first_node = nodes.pop(0)
            if first_node == '#':
                return
            root = TreeNode(int(first_node))
            
            root.left = helper(nodes)
            root.right = helper(nodes)
            
            return root
        
        nodes = data.split(",")
        # nodes的最后一个元素是空string，因为最后一个char 是逗号，所以split 出来会多一个空string。
        # 但是这不影响我们的操作。因为在填满所有的空和非空的node以后，就直接从return root return 了
        # 不需要回到开头check nodes 的地方。
        # 当然我们也可以直接remove 掉空string， before we passing in helper function
        return helper(nodes)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))