"""
 You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin. 
"""
from collections import defaultdict

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        MAX = float('inf')
        opt = [MAX] * (amount+1)
        opt[0] = 0
        for i in xrange(1,amount+1):
            
            for x in coins:
                if i-x >= 0:
                    opt[i] = min(opt[i],opt[i-x] + 1)
            
        return opt[amount] if opt[amount]!=MAX else -1
        
        
if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print s.coinChange(coins, amount)
    coins = [2]
    amount = 3
    print s.coinChange(coins, amount)






            
