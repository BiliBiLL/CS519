"""
 Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

Subscribe to see which companies asked this question.
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        opt = [False] * (len(s)+1)
        opt[0] = True
        j =0 
        for i in xrange(1,len(s)+1):
            for j in xrange(i):
                if opt[i] == True:continue
                opt[i] = opt[j] and (s[j:i] in wordDict)
            #if opt[i] == True: j = i
        print opt        
        return opt[len(s)]
                
                
if __name__ == "__main__":
    cls = Solution()
    s = "aaaaaaa"
    dic = ["aaaa", "aaa"]
    print cls.wordBreak(s,dic)
    
    
    
    
"""
Note: This problem is not quite easy. First opt record whether the previous substring before i is found in dictionary, all we need to do is to find see the last opt, which is opt[-1]
"""
