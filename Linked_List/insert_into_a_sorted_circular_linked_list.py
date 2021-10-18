import math
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # # 设定条件的时候没有设定好，导致corner case永远cover不住
        # if not head:
        #     head = Node(insertVal)
        #     head.next = head
        #     return head
        
        # slow, fast = head, head.next
        # is_insert = False
        # while True:
        #     if slow.val <= insertVal <= fast.val:
        #         is_insert = True
        #     elif slow.val > fast.val:
        #         if insertVal > slow.val or insertVal < fast.val:
        #             is_insert = True
        #     if is_insert:
        #         tmp = Node(insertVal, next=fast)
        #         slow.next = tmp
        #         return head
        #     slow, fast = fast, fast.next
        #     if slow == head:
        #         break
        # slow.next = Node(insertVal, next=fast)
        # return head
        
# ******* 第二遍 ************
# case 1 and case2
# 在递增的区间内, 这个可以包含首尾相连的地方
# 1 -> 3 -> 4
# ^         |
# | -  -  - |

# insertval = 2
# output: 1 (2) 3 4

# case 2
# insert 到首尾相连的地方 在 circular linked list 里面
# 3 -> 4 -> 1
# ^         |
# | -  -  - |

# insertval = 2
# output: 3 4 1 (2)

# case 3:
# insert 到递增结束的地方
# 3 -> 4 -> 1
# ^         |
# | -  -  - |

# insertval = 0
# output: 3 4 (0) 1

# case 4 
# insert to anywhere is ok
# output: 3 3 (0) 3 or 3 (0) 3 3 or 3 3 3 (0)
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        left = head
        right = head.next
        in_loop = False
        while left != head or in_loop == False:
            in_loop = True
            # case 1 and case 2:
            if left.val <= insertVal <= right.val:
                temp = Node(insertVal)
                left.next = temp
                temp.next = right
                return head
            # case 3:
            elif left.val > right.val:
                if insertVal > left.val or insertVal < right.val:
                    temp = Node(insertVal)
                    left.next = temp
                    temp.next = right
                    return head
            left = right
            right = right.next
        
        # case 4:
        # 3 3 3 (0) or 3 (0) 3 3
        # temp = Node(insertVal)
        # slow.next = temp
        # temp.next = fast
        head_next = head.next
        temp = Node(insertVal)
        head.next = temp
        temp.next = head_next
        return head


    def call_function(self) -> None:
        head = Node(1)
        head.next = Node(3)
        head.next.next = Node(5)
        head.next.next.next = head
        self.insert(head, 0)