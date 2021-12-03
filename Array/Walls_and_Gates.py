from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def find_gates(rooms):
            gates = []
            for i in range(len(rooms)):
                for j in range(len(rooms[0])):
                    if rooms[i][j] == 0:
                        gates.append([i, j])
            return gates

        gates = find_gates(rooms)
        
        moves = [[1,0], [0, 1], [-1, 0], [0, -1]]
        m = len(rooms)
        n = len(rooms[0])
        for gate in gates:
            queue = deque()
            queue.append(gate)
            visited = set()
            visited.add((gate[0], gate[1]))
            steps = 0
            while queue:
                size = len(queue)
                steps += 1

                for i in range(size):
                    node = queue.popleft()
                    for move in moves:
                        r = node[0] + move[0]
                        c = node[1] + move[1]
                        
                        if 0 <= r < m \
                        and 0 <= c < n \
                        and (r, c) not in visited \
                        and rooms[r][c] != -1 \
                        and rooms[r][c] != 0:
                            rooms[r][c] = min(rooms[r][c], steps)
                            queue.append([r, c])
                            visited.add((r, c))
        
        return
        
        