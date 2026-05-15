class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                b = (r // 3) * 3 + c // 3
                digit = board[r][c]
                if digit in rows[r] or digit in cols[c] or digit in boxes[b]:
                    return False
                
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[b].add(digit)
        return True