
# Definition for a Node.
from typing import Mapping


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # def __init__(self):
    #     self.visited = {}
    # def getCloneNode(self, node: 'Node') -> 'Node':
    #     if not node:
    #         return 
    #     if node in self.visited:
    #         return self.visited[node]
    #     else:
    #         self.visited[node] = Node(node.val)
    #         return self.visited[node]
        
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     if not head:
    #         return head
        
    #     old_node = head
    #     new_node = Node(old_node.val)
    #     self.visited[old_node] = new_node
        
    #     while old_node:
    #         new_node.random = self.getCloneNode(old_node.random)
    #         new_node.next = self.getCloneNode(old_node.next)
        
    #         old_node = old_node.next
    #         new_node = new_node.next
        
    #     return self.visited[head]


    # def copyRandomList(self, head: 'Node') -> 'Node':
    # # 第二遍
    # # 这道题最主要的是需要有一个visited map 来记录哪个node 已经cloned了哪个还没有cloned。
    # # 然后while loop 从第一个node开始iterate，每一个node 都要new_node 都要check cloned or not
    #     def get_cloned_node(node, visited):
    #         if not node:
    #             return
    #         if node in visited:
    #             return visited[node]
    #         else:
    #             copied_node = Node(node.val)
    #             visited[node] = copied_node
    #             return visited[node]
        
    #     if not head:
    #         return 
    #     visited = {}
    #     old_node = head
    #     new_node = Node(old_node.val)
    #     visited[old_node] = new_node
    #     while old_node:
    #         new_node.next = get_cloned_node(old_node.next, visited)
    #         new_node.random = get_cloned_node(old_node.random, visited)
            
    #         old_node = old_node.next
    #         new_node = new_node.next
        
    #     return visited[head]

    # 第三遍
    # 只需要一个origin node -> copied node 一个Mapping
    # 每一次iterate到一个新的node就需要check 这个node 在不在mapping 里。不在create 新的，在就直接return
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def get_cloned_node(node, visited):
            if not node:
                return 
            if node in visited:
                return visited[node]
            else:
                new_node = Node(node.val)
                visited[node] = new_node
                return new_node
            
        if not head:
            return None
        visited = {}
        origin = head

        while origin:
            cp_cur = get_cloned_node(origin, visited)

            cp_next = get_cloned_node(origin.next, visited)
            cp_random = get_cloned_node(origin.random, visited)

            cp_cur.next = cp_next
            cp_cur.random = cp_random
            
            origin = origin.next
        
        return visited[head]