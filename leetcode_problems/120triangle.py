"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        opt = [[0]*i for i in range(1,len(triangle)+1)]
        opt[0][0] = triangle[0][0]
        
        for i in xrange(1,len(triangle)):
            for j in xrange(i+1):
                if j ==0:
                    
                    opt[i][j] = opt[i-1][j] + triangle[i][j]
                elif j == i:
                    
                    opt[i][j] = opt[i-1][j-1] + triangle[i][j]
                if j > 0 and j < i:
                    
                    opt[i][j] = min(opt[i-1][j],opt[i-1][j-1]) + triangle[i][j]
                    
        return min(opt[-1])
        
        
        
        
if __name__ == "__main__":
    cls = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print cls.minimumTotal(triangle)
    triangle = [[-10]]
    print cls.minimumTotal(triangle)
    
    
    
