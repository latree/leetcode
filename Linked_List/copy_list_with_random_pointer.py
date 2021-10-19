
# Definition for a Node.
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


    def copyRandomList(self, head: 'Node') -> 'Node':
    # 第二遍
    # 这道题最主要的是需要有一个visited map 来记录哪个node 已经cloned了哪个还没有cloned。
    # 然后while loop 从第一个node开始iterate，每一个node 都要new_node 都要check cloned or not
        def get_cloned_node(node, visited):
            if not node:
                return
            if node in visited:
                return visited[node]
            else:
                copied_node = Node(node.val)
                visited[node] = copied_node
                return visited[node]
        
        if not head:
            return 
        visited = {}
        old_node = head
        new_node = Node(old_node.val)
        visited[old_node] = new_node
        while old_node:
            new_node.next = get_cloned_node(old_node.next, visited)
            new_node.random = get_cloned_node(old_node.random, visited)
            
            old_node = old_node.next
            new_node = new_node.next
        
        return visited[head]