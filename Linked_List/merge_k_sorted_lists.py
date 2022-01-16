from Data_Structure.list_node import ListNode
from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # # 一定要审题给的lists 其实是[head, head, head]， 不是[[ListNode, ListNode], [ListNode,ListNode]]
        # if not lists:
        #     return
        # m = len(lists)
        # # 其实这道题本身并不难，难的地方在于定义heap_list里面每一个item的是什么
        # # every element should be (c_node.val, r, c_node)
        # heap_list = []
        # dummy_head = ListNode(-1)
        # tail = dummy_head
        # # key: r, val: c_node
        # ptr_map = {}
        # for i in range(m):
        #     if lists[i]:
        #         cur_node = lists[i]
        #         ptr_map[i] = cur_node
        #         heapq.heappush(heap_list, (cur_node.val, i, cur_node))
                
        # while ptr_map:
        #     val, r, node = heapq.heappop(heap_list)
        #     tail.next = node
        #     tail = tail.next
            
        #     n_node = node.next
        #     if not n_node:
        #         del ptr_map[r]
        #     else:
        #         n_item = (n_node.val, r, n_node)
        #         heapq.heappush(heap_list, n_item)
            
        # return dummy_head.next
            
            
        # # ************* important **********************
        # # ************* 这是第二次犯同样的错误了！！！！！！！！ **********************
        # # 一定要审题给的lists 其实是[head, head, head]， 不是[[ListNode, ListNode], [ListNode,ListNode]]
        # # 其实这道题本身并不难，难的地方在于定义heap_list里面每一个item的是什么
        # if not lists:
        #     return
        
        # m = len(lists)
        
        # dummy = ListNode(-99999)
        # cur = dummy
        # ptrs = {}

        # heap_list = []
        # for i in range(m):
        #     if not lists[i]:
        #         continue
        #     ptrs[i] = lists[i]
        #     # ************* important **********************
        #     # heap compare 的key 默认的是tuple 里面的第一个元素。而且heap compare的key 是无法customize的
        #     heapq.heappush(heap_list, (lists[i].val, i, lists[i]))
        
        # while ptrs:
        #     value, row, cur_node = heapq.heappop(heap_list)
        #     # update ptrs next ptr in this current linkedd list
        #     ptrs[row] = cur_node.next
        #     if not cur_node.next:
        #         del ptrs[row]
        #     else:
        #         # add new element into priority queue
        #         next_node = ptrs[row]
        #         heapq.heappush(heap_list, (next_node.val, row, next_node))
            
        #     # create Node and insert to final list
        #     temp = ListNode(value)
        #     cur.next = temp
        #     cur = cur.next
        
        # return dummy.next

    # 第三遍：
    # 同样的审题错误导致写完以后又要重新改代码。跟第二次犯的错误是一样的
        if not lists:
            return
        idx_map = {}
        dummy = ListNode(-1)
        cur = dummy
        last_modified_idx = -1
        heap = []

        for i in range(len(lists)):
            if not lists[i]:
                continue
            idx_map[i] = lists[i]
            heapq.heappush(heap, (lists[i].val, i))

            
        while idx_map:
            if last_modified_idx != -1:
                cur_node = idx_map[last_modified_idx]
                heapq.heappush(heap, (cur_node.val, last_modified_idx))

            val, cur_idx = heapq.heappop(heap)
            temp_node = idx_map[cur_idx]
            idx_map[cur_idx] = idx_map[cur_idx].next
            last_modified_idx = cur_idx
            
            if not idx_map[cur_idx]:
                del idx_map[cur_idx]
                last_modified_idx = -1
                
            cur.next = temp_node
            cur = cur.next
            
        return dummy.next