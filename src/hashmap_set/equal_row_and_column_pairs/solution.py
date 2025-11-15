from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        hash = defaultdict(int)

        for row in grid:
            hash[str(row)] += 1

        for col_index in range(len(grid[0])):
            col = []
            for row_index in range(len(grid)):
                col.append(grid[row_index][col_index])
            count += hash[str(col)]

        return count
