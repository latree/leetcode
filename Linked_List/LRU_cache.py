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



# orderedDict version
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order_dict = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.order_dict:
            return -1
        self.order_dict.move_to_end(key)
        return self.order_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.order_dict:
            self.order_dict.move_to_end(key)
        self.order_dict[key] = value
        if len(self.order_dict) > self.capacity:
            self.order_dict.popitem(last = False)
