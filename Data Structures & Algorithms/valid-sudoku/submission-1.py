class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        boxes = [set() for _ in range(len(board))]

        for r in range(len(rows)):
            for c in range(len(cols)):
                val = board[r][c]

                if val == ".":
                    continue
                
                box_id = (r // 3) * 3 + (c // 3)

                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_id]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)
        
        print(boxes)
        return True