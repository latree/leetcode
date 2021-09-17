from Data_Structure.list_node import ListNode
from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 一定要审题给的lists 其实是[head, head, head]， 不是[[ListNode, ListNode], [ListNode,ListNode]]
        if not lists:
            return
        m = len(lists)
        # 其实这道题本身并不难，难的地方在于定义heap_list里面每一个item的是什么
        # every element should be (c_node.val, r, c_node)
        heap_list = []
        dummy_head = ListNode(-1)
        tail = dummy_head
        # key: r, val: c_node
        ptr_map = {}
        for i in range(m):
            if lists[i]:
                cur_node = lists[i]
                ptr_map[i] = cur_node
                heapq.heappush(heap_list, (cur_node.val, i, cur_node))
                
        while ptr_map:
            val, r, node = heapq.heappop(heap_list)
            tail.next = node
            tail = tail.next
            
            n_node = node.next
            if not n_node:
                del ptr_map[r]
            else:
                n_item = (n_node.val, r, n_node)
                heapq.heappush(heap_list, n_item)
            
        return dummy_head.next
            
        