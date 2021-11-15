from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            res = []
            for i in range(n):
                cur_row = []
                for j in range(n):
                    if j == state[i]:
                        cur_row.append("Q")
                    else:
                        cur_row.append(".")
                res.append("".join(cur_row))
            return res
            
        
        def dfs(n, row, state, res, diagonals, anti_diagonals):
            if row == n:
                board = create_board(state)
                res.append(board)
                return
            
            for col in range(n):                
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if col not in state and curr_diagonal not in diagonals and curr_anti_diagonal not in anti_diagonals:
                    state.append(col)
                    diagonals.add(curr_diagonal)
                    anti_diagonals.add(curr_anti_diagonal)
                    dfs(n, row + 1, state, res, diagonals, anti_diagonals)
                    diagonals.remove(curr_diagonal)
                    anti_diagonals.remove(curr_anti_diagonal)
                    state.pop()

        state = []
        res = []
        diagonals = set()
        anti_diagonals = set()
        dfs(n, 0, state, res, diagonals, anti_diagonals)
        
        return res
