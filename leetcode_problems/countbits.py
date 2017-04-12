# coding: utf-8
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2].
Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Hint:
You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        opt = {0:0}
        for i in xrange(1,num+1):
            opt[i] = opt[i>>1] + (i&1)
            #print i,opt[i>>1],i&1,opt[i>>1] + (i&1)
        res = []
        for i in xrange(num+1):
            res.append(opt[i])
        
        return res
        
        
        
if __name__ == "__main__":
    num = 5
    s = Solution()
    print s.countBits(num)
    
    
"""
This case is interesting, opt[n] = opt[n/2] + (n's last digit)   
***Note that, "opt[i>>1] + i & 1" is wrong, plus will calculate first, so remember the bracket.
how to define whether the last digit of a number is 0 or 1? simple (num & 1)
"""

