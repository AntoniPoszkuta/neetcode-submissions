class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0
        cords = [[0,1],[1,0],[-1,0],[0,-1]]
        max_x = len(grid)
        max_y = len(grid[0])
        max_area = 0
        area = 0 

        def find_island(x, y):
            nonlocal area
            area += 1
            grid[x][y] = 0
            for nx, ny in cords:
                if 0 <= x + nx < max_x and 0 <= y + ny < max_y and grid[x + nx][y + ny] == 1:
                    find_island(x + nx, y + ny) 
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    find_island(x,y)
                    if area > max_area:
                        max_area = area
                    area = 0
        
        return max_area