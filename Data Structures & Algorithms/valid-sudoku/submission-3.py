class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROW = defaultdict(set)
        COLS = defaultdict(set)
        SQR = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in ROW[r] or board[r][c] in COLS[c] or board[r][c] in SQR[(r//3,c//3)]):
                    return False
                COLS[c].add(board[r][c])
                ROW[r].add(board[r][c])
                SQR[(r//3, c//3)].add(board[r][c])

        return True







        