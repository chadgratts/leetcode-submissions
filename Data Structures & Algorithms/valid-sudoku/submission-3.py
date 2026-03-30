class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: list of sublists
        # output: boolean

        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                b = (r // 3) * 3 + (c // 3)

                if v != ".":
                    if v in rows[r]:
                        return False
                    if v in cols[c]:
                        return False
                    if v in boxes[b]:
                        return False

                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[b].add(v)
        
        return True