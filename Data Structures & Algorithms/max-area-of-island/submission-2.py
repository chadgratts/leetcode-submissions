class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            visited.add((r, c))
            queue = collections.deque()
            queue.append((r, c))
            curr_area = 1

            while queue:
                ir, ic = queue.popleft()
                for nr, nc in neighbors:
                    if (
                        0 <= nr + ir < row and
                        0 <= nc + ic < col and
                        (ir + nr, ic + nc) not in visited and
                        grid[ir + nr][ic + nc] == 1
                    ):
                        visited.add((ir + nr, ic + nc))
                        queue.append((ir + nr, ic + nc))
                        curr_area += 1
            return curr_area

        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area