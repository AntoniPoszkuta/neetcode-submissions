class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        while l <= r:
            mid = (r + l) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][n]:
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        if (mid < 0 or mid > len(matrix) - 1) or (l > r):
            return False
        

        array = matrix[mid]

        l = 0
        r = len(array) - 1
        while l <= r:
            mid = (r + l) // 2

            if array[mid] == target:
                return True
            elif target > array[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
 