class Solution:
    def isnt_equal(self, lis):
        return len(lis) != len(set(lis))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                boxes[r // 3 + (c // 3)*3].append(board[r][c])

        for x in range(9):
            if self.isnt_equal(rows[x]) or self.isnt_equal(cols[x]) or self.isnt_equal(boxes[x]):
                return False

        return True