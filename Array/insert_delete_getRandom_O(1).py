import random 
class RandomizedSet:

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.val_idx_map = {}
    #     self.val_list = []

    # def insert(self, val: int) -> bool:
    #     """
    #     Inserts a value to the set. Returns true if the set did not already contain the specified element.
    #     """
    #     if val not in self.val_idx_map:
    #         self.val_list.append(val)
    #         self.val_idx_map[val] = len(self.val_list) - 1
    #         return True
    #     else:
    #         return False

    # def remove(self, val: int) -> bool:
    #     """
    #     Removes a value from the set. Returns true if the set contained the specified element.
    #     """
    #     if val in self.val_idx_map:
    #         tmp_idx = self.val_idx_map[val]
    #         # 这个swap then pop 的操作在最开始的时候没有想到
    #         self.val_list[tmp_idx], self.val_list[-1] = self.val_list[-1], self.val_list[tmp_idx]
    #         self.val_idx_map[self.val_list[tmp_idx]] = tmp_idx
    #         del self.val_idx_map[val]
    #         self.val_list.pop()
    #         return True
    #     else:
    #         return False
        

    # def getRandom(self) -> int:
    #     """
    #     Get a random element from the set.
    #     """
    #     idx = random.randint(0, len(self.val_list) - 1)
    #     return self.val_list[idx]


    def __init__(self):
        self.array = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        else:
            self.array.append(val)
            self.idx_map[val] = len(self.array) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            val_idx = self.idx_map[val]
            # ******************* import ***********************
            # swap 到array的末尾开始的时候还是没有反应过来。第二次没有反应过来 
            # swap to end of list
            self.array[val_idx], self.array[-1] = self.array[-1], self.array[val_idx]
            self.idx_map[self.array[val_idx]] = val_idx
            self.array.pop()
            del self.idx_map[val]
            return True
        return False

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.array) - 1)
        return self.array[idx]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert","getRandom"]
# [[],                [1],      [2],      [2],        [],         [1],     [2],      []]
#  [null,             true,     false,    true,       2,          true,   false,      2]
    
    
    
