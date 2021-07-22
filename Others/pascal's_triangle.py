from typing import List

class pascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        # solution 1: straight forward
        if numRows < 1:
            return []
        
        res = [[1]]
        for i in range(1, numRows):
            open_one = 1
            close_one = 1
            last_ele_length = len(res[-1])
            cur_row = [open_one]
            j = 0
            while j + 1 < last_ele_length:
                cur_row.append(res[-1][j] + res[-1][j + 1])
                j += 1
            cur_row.append(close_one)
            res.append(cur_row)
        
        return res