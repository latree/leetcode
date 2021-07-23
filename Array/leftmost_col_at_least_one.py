from Data_Structure import binary_matrix
from Data_Structure.binary_matrix import BinaryMatrix
from typing import List
import math

class leftMostColumnWithOne:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def bin_search(matrix: BinaryMatrix, row: int, col: int) -> int:
            left, right = 0,  col - 1
            while left < right:
                mid = (left + right) // 2
                if matrix.get(row, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            
            return left if matrix.get(row, left) == 1 else math.inf

        [row, col] = binaryMatrix.dimensions()
        min_idx = math.inf
        for i in range(row):
            left_most_idx = bin_search(binaryMatrix, i, col)
            min_idx = min(min_idx, left_most_idx)

        return min_idx if min_idx != math.inf else -1


    def call_function(self) -> None:
        return self.leftMostColumnWithOne(BinaryMatrix(3,4))



# [
# [0,0,0,1],
# [0,0,1,1],
# [0,1,1,1]
# ]