"""
 Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit = bin(n)
        if len(bit) < 4:
            #print "haha"
            return bit[2] == '1'
        for x in bit[3:]:
            print "ye"
            if x == '1':return False
            
        return (bit[2] == '1')
        
if __name__ == "__main__":
    cls = Solution()
    print cls.isPowerOfTwo(3)
