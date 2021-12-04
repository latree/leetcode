from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # 这是一个数学问题。三点之间最近的距离就应该是他们的中位数。
        def find_building_points(grid):
            rows, cols = [], []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        rows.append(i)
                        cols.append(j)
            return rows, cols
        
        
        def get_median(rows, cols):
            rows.sort()
            cols.sort()
            
            median_row = rows[len(rows) // 2]
            median_col = cols[len(cols) // 2]
            
            return median_row, median_col
        
        
        rows, cols = find_building_points(grid)
        m_row, m_col = get_median(rows, cols)
        
        res = 0
        
        for x in rows:
            res += abs(m_row - x)
        
        for y in cols:
            res += abs(m_col - y)
            
    
        return res
        
        