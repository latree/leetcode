class BinaryMatrix(object):
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.matrix = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
        # self.matrix = [[] for _ in range(row)]
        # for i in range(len(row)):
        #     self.matrix[i] = [0 for _ in range(col)]
        
    def get(self, row: int, col: int) -> int:
       return self.matrix[row][col]

    def dimensions(self) -> list[int, int]:
       return [self.row, self.col]