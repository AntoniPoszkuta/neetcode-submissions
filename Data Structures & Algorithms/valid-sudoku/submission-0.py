class Solution:
    def check_col(self, board, index):
        nums = []

        for x in range(9):
            if board[x][index] == ".":
                continue
            
            nums.append(board[x][index])

        return True if len(nums) == len(set(nums)) else False

    def check_row(self, board, index):
        nums = []

        for x in range(9):
            if board[index][x] == ".":
                continue 
            
            nums.append(board[index][x])

        return True if len(nums) == len(set(nums)) else False

    def check_box(self, board, r_off, c_off):
        nums = []

        for r in range(3):
            for c in range(3):
                if board[r_off + r][c_off + c] == ".":
                    continue
                nums.append(board[r_off + r][c_off + c])

        return True if len(nums) == len(set(nums)) else False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for num in range(9):
            if not self.check_row(board, num) or not self.check_col(board, num):
                return False
        
        for r in range(3):
            for c in range(3):
                if not self.check_box(board,r*3,c*3):
                    return False

        return True

        