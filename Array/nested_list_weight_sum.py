from typing import List
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # 每一层的data type 是List[NestedInteger]，而不是NestedInteger[NestedInteger]
        # 开始的时候有些混淆
#         solution 1: BFS
#         res = 0 
#         depth = 0
#         queue = Deque()        
#         for item in nestedList:
#             queue.append((item, 1))

        
#         while queue:
#             cur_item, cur_depth = queue.popleft()
#             if not cur_item.isInteger():
#                 for nested_item in cur_item.getList():
#                     queue.append((nested_item, cur_depth + 1))
#             else:
#                 res += cur_item.getInteger() * cur_depth
        
#         return res
        
        def dfs(item, depth):
            if item.isInteger():
                return item.getInteger() * depth
            res = 0            
            for nested_item in item.getList():
                res += dfs(nested_item, depth + 1)
            
            return res
                
        res = 0
        for item in nestedList:
            res += dfs(item, 1)
        
        return res



# 第二遍心得：
# 之前有一个错误的地方在于不适用return value，直接把res pass成param
# 但是有一个special case 不能被catch，就是最开始的 integer item 会被忽略
# 比如这个case 的中间的那个 value 2 [[1,1],2,[1,1]]
# 因为
# if nested_ele.isInteger():
#     cur_sum += nested_ele.getInteger() * depth
#     return
# 这个cur_sum 在计算完以后没有被加到res里面去。如果是第一层的NestedInteger