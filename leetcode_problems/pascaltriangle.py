"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = [[1]]
        for i in range(numRows -1):
            temp = [x+y for x,y in zip([0]+tri[i],tri[i] + [0])]
            tri.append(temp)
        
        return tri
	

if __name__ == "__main__":
    s = Solution()
    print s.generate(3)
    print s.generate(5)
    print s.generate(7)
