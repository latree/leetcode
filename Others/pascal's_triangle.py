from typing import List

class pascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        # solution 1: straight forward
        if numRows < 1:
            return []
        
        res = [[1]]
        for _ in range(1, numRows]):
            
