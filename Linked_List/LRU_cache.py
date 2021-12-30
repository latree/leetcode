from typing import ChainMap
from collections import OrderedDict


class DLinkedNode:
    def __init__(self, key, val: int, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.head = DLinkedNode(-1, -1)
    #     self.tail = DLinkedNode(-1, -1)
    #     self.node_map = {}
    #     self.head.next = self.tail
    #     self.tail.prev = self.head

    # def get(self, key: int) -> int:
    #     if key in self.node_map:
    #         self._remove_node(self.node_map[key])
    #         self._add_node(self.node_map[key])
    #         return self.node_map[key].val
    #     else:
    #         return -1        

    # def put(self, key: int, value: int) -> None:
    #     if key in self.node_map:
    #         self.node_map[key].val = value
    #         self._remove_node(self.node_map[key])
    #         self._add_node(self.node_map[key])

    #     else:
    #         if len(self.node_map) >= self.capacity:
    #             # delete the first node if capacity is reached
    #             if len(self.node_map) > 0:
    #                 self.node_map.pop(self.head.next.key)
    #                 self._remove_node(self.head.next)

    #         self.node_map[key] = DLinkedNode(key, value)
    #         self._add_node(self.node_map[key])

    # def _add_node(self, node) -> None:
    #     node.prev = self.tail.prev
    #     node.prev.next = node
    #     node.next = self.tail
    #     self.tail.prev = node

    # def _remove_node(self, node) -> None:
    #     cur_prev = node.prev
    #     cur_next = node.next
    #     cur_prev.next = cur_next
    #     cur_next.prev = cur_prev
        

    # def call_function(self) -> None:
    #     self.put(2, 1)
    #     self.put(1, 1)
    #     self.put(2, 3)
    #     self.put(4, 1)
    #     self.get(1)
    #     self.get(2)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# # ********** important ******************
# # orderedDict version
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.order_dict = OrderedDict()
        
#     def get(self, key: int) -> int:
#         if key not in self.order_dict:
#             return -1
#         self.order_dict.move_to_end(key)
#         return self.order_dict[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.order_dict:
#             self.order_dict.move_to_end(key)
#         self.order_dict[key] = value
#         if len(self.order_dict) > self.capacity:
#             self.order_dict.popitem(last = False)


# # 第二遍
# class DlinkedNode:
#     def __init__(self, key, val, prev=None, next=None):
#         self.key = key
#         self.val = val
#         self.prev = prev
#         self.next = next

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.node_map = {}
#         self.head = DlinkedNode(-1, -1)
#         self.tail = DlinkedNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key: int) -> int:
#         if key not in self.node_map:
#             return -1
        
#         node = self.node_map[key]
#         self.remove_node(node)
#         self.add_node(node)
#         return node.val
        

#     def put(self, key: int, value: int) -> None:
#         if key not in self.node_map:
#             if len(self.node_map) >= self.cap:
#                 # ********* important ***********
#                 # 这里非常容易出错。必须要先pop node_map里的key 然后再delete node
#                 # 因为如果先delete node 以后那么self.tail.prev 就会改变。那么self.tail.prev.key也会改变，那么就回pop错value
#                 self.node_map.pop(self.tail.prev.key)
#                 self.remove_node(self.tail.prev)
#             node = DlinkedNode(key, value)
#             self.add_node(node)
#             self.node_map[key] = node
#         else:
#             node = self.node_map[key]
#             node.key = key
#             node.val = value
#             self.remove_node(node)
#             self.add_node(node)

    
#     def add_node(self, node):
#         node.next = self.head.next
#         node.prev = self.head
#         node.next.prev = node
#         node.prev.next = node
    
#     def remove_node(self, node):
#         cur_prev = node.prev
#         cur_next = node.next
#         cur_prev.next = cur_next
#         cur_next.prev = cur_prev


# 第二遍： OrderedDict
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]    

    def put(self, key: int, value: int) -> None:
        # ********** important ************
        # 简化了这里的步骤。 不管key在不在这里，都应该直接update key value ，然后move到最后
        # 最后如果多了就pop最前面的
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)