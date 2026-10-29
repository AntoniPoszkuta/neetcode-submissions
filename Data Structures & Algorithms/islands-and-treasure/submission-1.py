from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        cords = ([0,1],[0,-1],[1,0],[-1,0])


        queue = deque()
        steps = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    queue.append([x,y])
        
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                x, y = queue.popleft()
                grid[x][y] = steps
                for nx, ny in cords:
                    if 0 <= x + nx < len(grid) and 0 <= y + ny < len(grid[0]) and grid[x + nx][y + ny] == 2147483647:
                        queue.append([x + nx, y + ny])
                        grid[x + nx][y + ny] = -1

            steps += 1
