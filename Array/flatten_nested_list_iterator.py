from typing import List
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> List[NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        # 注意需要打印的顺序。
        self.cur_stack = nestedList[::-1].copy()
    
    def next(self) -> int:
        return self.cur_stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.cur_stack and not self.cur_stack[-1].isInteger():
            # 注意需要打印的顺序。
            nested_integers = self.cur_stack.pop().getList()[::-1]
            for nested_integer in nested_integers:
                self.cur_stack.append(nested_integer)
        
        return len(self.cur_stack) != 0
                
                
            
            

            

            
            
            
            
            
            
            
            
            
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())