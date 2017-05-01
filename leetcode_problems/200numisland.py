"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None:return 0
        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    self.dfs(grid,i,j)
        return count
        
    def dfs(self,grid,i,j):
        if 0<=i or i<len(grid) or 0<=j or j<len(grid[0]) or grid[i][j] == 1:
            grid[i][j] = 0
            
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)      
        
        return       
            
            
            
