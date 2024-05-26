class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cross = defaultdict(int)
        cnt = 0

        for row in grid:
            cross[str(row)] += 1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += cross[str(col)]
        return cnt