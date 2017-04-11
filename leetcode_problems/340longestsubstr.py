class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = [0] *200
        length = len(s)
        maxlen = 0
        count = 0
        distinct = 0
        l = 0
        if k == 0:
            return 0
        for r in xrange(length):
            
            count += 1
            
            if dic[ord(s[r])] == 0:
                dic[ord(s[r])] += 1
                distinct += 1
                if distinct > k:
                    #print count
                    maxlen = max(count -1,maxlen)
                    #print "maxlen",maxlen
                    while distinct > k and l < r:
                        dic[ord(s[l])] -= 1
                        if dic[ord(s[l])] == 0: distinct -= 1
                        
                        count -= 1
                        print "subtract",count
                        l += 1
            else:
                dic[ord(s[r])] += 1
        #print distinct
        maxlen = max(count,maxlen)
        return maxlen
            
            
if __name__ == "__main__":
    a = Solution()
    s = "abcdefg"
    #print a.lengthOfLongestSubstringKDistinct(s,1)
    #s = "aabceff#dddd"
    s = "a"
    print a.lengthOfLongestSubstringKDistinct(s,0)    #aabc           
                    
                        
"""
Conclusion: I think I need 
"""
                 
                
