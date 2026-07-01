class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQR = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col]=='.':
                    continue
                if board[row][col] in ROWS[row] or board[row][col] in COLS[col] or board[row][col] in SQR[(row//3, col//3)]:
                    return False
                
                ROWS[row].add(board[row][col])
                COLS[col].add(board[row][col])
                SQR[(row//3, col//3)].add(board[row][col])

        return True
        