class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        cords = ([0,1],[0,-1],[1,0],[-1,0])
        
        queue = deque()
        fruits = 0
        steps = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append([x,y])
                    fruits += 1
                elif grid[x][y] == 1:
                    fruits += 1
        
        
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                x, y = queue.popleft()
                grid[x][y] = 0
                fruits -= 1
                for nx, ny in cords:
                    if 0 <= x + nx < len(grid) and 0 <= y + ny < len(grid[0]) and grid[x + nx][y + ny] == 1:
                        queue.append([x + nx, y + ny])
                        grid[x + nx][y + ny] = 0

            steps += 1
        
        return steps-1 if fruits == 0 else -1
    
