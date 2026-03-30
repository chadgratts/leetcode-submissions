class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                cell = board[r][c]
                b = (r // 3, c // 3)
                # 0, 1, 2 | 0, 1, 2

                if (cell in rows[r]
                    or cell in cols[c]
                    or (b, cell) in boxes):

                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                boxes.add((b, cell))
        return True