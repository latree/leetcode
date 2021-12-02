class TicTacToe:
    # 这道题最巧妙的地方是在于每一行，每一列，正对角线，反对角线 只需要用一个数来代表
    # player 1 就是+1 player 2 就是-1， 只要以上的四种方式有sum == n 或者-n 那么就是有一方赢了
    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        offset = 1 if player == 1 else - 1
        self.row[row] += offset
        self.col[col] += offset
        
        if row + col == self.n - 1:
            self.anti_diag += offset
        if row - col == 0:
            self.diag += offset
        
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)