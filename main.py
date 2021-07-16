# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# from Tree.validate_binary_search_tree import ValidBST
# from Tree.symmetric_tree import SymmetricTree
# from Tree.binary_bree_level_order_traversal import LevelOrder
# from Tree.convert_sorted_tree_to_bst import sortedArrayToBST
# from DP.climbing_stairs import climbStairs
# from DP.best_ime_buy_sell_stock import maxProfit
# from DP.maximum_subarray import maxSubArray
# from DP.house_robber import Rob
from Design.min_stack import MinStack

if __name__ == '__main__':

    # Rob().call_function()
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    
    obj.getMin()
    obj.pop()
    obj.top()
    obj.getMin()