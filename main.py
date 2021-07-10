# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Data_Structure.tree_node import TreeNode
from Tree.validate_binary_search_tree import ValidBST

if __name__ == '__main__':

    root = TreeNode(2147483647)


    print(ValidBST().isValidBST(root))