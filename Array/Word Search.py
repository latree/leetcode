class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, r, c, visited, word, idx, moves):
            if idx == len(word) - 1:
                if board[r][c] == word[idx]:
                    return True
                else:
                    return False
                
            
            if board[r][c] != word[idx]:
                return False
            
            visited.add((r, c))
            
            for move in moves:
                n_r, n_c = r + move[0], c + move[1]
                
                if 0 <= n_r < len(board) and 0 <= n_c < len(board[0]) and (n_r, n_c) not in visited:
                    if dfs(board, n_r, n_c, visited, word, idx + 1, moves):
                        return True
            visited.remove((r, c))
            return False
        
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    
                    if dfs(board, i, j, visited, word, 0, moves):
                        return True
        
        return False
