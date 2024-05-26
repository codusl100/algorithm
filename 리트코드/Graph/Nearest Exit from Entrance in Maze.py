class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        q = collections.deque([entrance + [0]])
        while q:
            y, x, count = q.popleft()
            if (x in (0, N-1) or y in (0, M-1)) and [y, x] != entrance:
                return count
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < N and 0 <= ny < M and maze[ny][nx] == ".":
                    maze[ny][nx] = '+'
                    q.append([ny, nx, count + 1])
                    
        return -1