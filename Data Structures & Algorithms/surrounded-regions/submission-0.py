class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        
        for x in range(1,len(board) - 1):
            for y in range(1,len(board[0]) - 1):
                board[x][y] = "X"
        