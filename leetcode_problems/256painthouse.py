"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        opt = {0:[0,0,0]}
        
        for i,x in enumerate(costs):
            opt[i] = [costs[i][j] + min(opt[i][:j] + opt[i][j+1:]) for j in range(3)]
            
        return min(opt[len(costs)-1])
"""
        prev = [0] * 3
        for now in costs:
            prev = [now[i] + min(prev[:i] + prev[i+1:]) for i in range(3)]
        return min(prev)
"""
        
if __name__ == "__main__":
    cls = Solution()
    costs = [[1,2,3],[2,1,1]]
    print cls.minCost(costs)
