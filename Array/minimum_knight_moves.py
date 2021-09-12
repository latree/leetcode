class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Time: O(max(2|x|, 2|y|) ^2). Max reach out area is max(2|x|, 2|y|)^2
        # space: O(max(2|x|, 2|y|) ^2)
        directions = [(2, 1), (1, 2), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        queue = deque()
        queue.append((0, 0))
        visited = set()
        steps = 0
        while queue:
            cur_level_size = len(queue)

            for i in range(cur_level_size):
                c_x, c_y = queue.popleft()
                if c_x == x and c_y == y:
                    return steps
                
                for direction in directions:
                    n_x, n_y = c_x + direction[0], c_y + direction[1]
                    if (n_x, n_y) not in visited:
                        visited.add((n_x, n_y))
                        queue.append((n_x, n_y))
            steps += 1
        
        return steps