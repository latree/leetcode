class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 这道题最关键的两个地方
        # 1.用recursion 做了一个 嵌套for loop 遍历matrix 的方法。这个方法要记住
        # 2.每一个 有dot的地方可以有9个分枝，通过is_valid 来砍枝
        #   至于层数就是遍历每一个dot（也就是matrix空的地方）， 有多少个dot，就有多少层
        
        def is_valid(board, r, c, ch):
            for i in range(9):
                if board[i][c] == ch:
                    return False
                if board[r][i] == ch:
                    return False
            
            c_r = r - (r % 3)
            c_c = c - (c % 3)
            for i in range(c_r, c_r + 3):
                for j in range(c_c, c_c + 3):
                    if board[i][j] == ch:
                        return False
            return True
        
        
        def dfs(board, i, j, board_size):
            if j == board_size:
                return dfs(board, i + 1, 0, board_size)
            
            if i == board_size:
                return True
            
            if board[i][j] != '.':
                return dfs(board, i, j + 1, board_size)
                
            
            for ch in range(1, board_size + 1):
                if not is_valid(board, i, j, str(ch)):
                    continue
                board[i][j] = str(ch)
                if dfs(board, i, j + 1, board_size):
                    return True
                board[i][j] = '.'
            return False
        
        return dfs(board, 0, 0, 9)
                