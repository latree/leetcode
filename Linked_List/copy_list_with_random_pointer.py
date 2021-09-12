
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}
    def getCloneNode(self, node: 'Node') -> 'Node':
        if not node:
            return 
        if node in self.visited:
            return self.visited[node]
        else:
            self.visited[node] = Node(node.val)
            return self.visited[node]
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        old_node = head
        new_node = Node(old_node.val)
        self.visited[old_node] = new_node
        
        while old_node:
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)
        
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]
        