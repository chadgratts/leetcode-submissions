class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = set()
        max_area = [0]

        def bfs(r, c, max_area):
            visited.add((r, c))
            queue = collections.deque()
            queue.append((r, c))
            curr_area = 1

            while queue:
                ir, ic = queue.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    if (
                        ir + dr in range(row) and
                        ic + dc in range(col) and
                        (ir + dr, ic + dc) not in visited and
                        grid[ir + dr][ic + dc] == 1
                    ):
                        visited.add((ir + dr, ic + dc))
                        queue.append((ir + dr, ic + dc))
                        curr_area += 1
            max_area[0] = max(max_area[0], curr_area)

        for r in range(row):
            for c in range(col):
                if grid[r][c] not in visited and grid[r][c] == 1:
                    bfs(r, c, max_area)
        
        return max_area[0]