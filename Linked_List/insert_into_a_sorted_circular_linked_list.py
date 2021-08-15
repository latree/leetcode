import math
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # 设定条件的时候没有设定好，导致corner case永远cover不住
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        slow, fast = head, head.next
        is_insert = False
        while True:
            if slow.val <= insertVal <= fast.val:
                is_insert = True
            elif slow.val > fast.val:
                if insertVal > slow.val or insertVal < fast.val:
                    is_insert = True
            if is_insert:
                tmp = Node(insertVal, next=fast)
                slow.next = tmp
                return head
            slow, fast = fast, fast.next
            if slow == head:
                break
        slow.next = Node(insertVal, next=fast)
        return head
        
    def call_function(self) -> None:
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(5)
        head.next.next.next = head
        self.insert(head, 0)
# 0
#      1    3    5       1
#                s       f
#      ms   mn

# # head = 3
# [3,4,1]
# 2

# 3   4    1   3
#          s    f
                    
