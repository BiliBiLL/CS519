"""
Now you are given a string S, which represents a software license key which we would like to format. The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly misplaced.

We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all the lower case letters in the string must be converted to upper case.

So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return the license key formatted according to the description above.

Example 1:

Input: S = "2-4A0r7-4k", K = 4

Output: "24A0-R74K"

Explanation: The string S has been split into two parts, each part has 4 characters.

Example 2:

Input: S = "2-4A0r7-4k", K = 3

Output: "24-A0R-74K"

Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it could be shorter as said above.

Note:

    The length of string S will not exceed 12,000, and K is a positive integer.
    String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
    String S is non-empty.
"""

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        newstr = [x for x in s if x != '-']
        group = len(newstr)/k
        headlen = len(newstr)%k
        output = ""
        if headlen == 0 and group == 1: #only k elements exist
            return output.join(str(e) for e in newstr).upper()
            #return output
        elif headlen == 0 and group > 1:
            for i in xrange(group-1,0,-1):
                newstr.insert(i*k,'-') 
            return output.join(str(e) for e in newstr).upper() #elements can be divide by k evenly
            #return output
        elif group == 0:
            return output.join(str(e) for e in newstr).upper()
        else:
            temp = []
            newstr
            
            for i in xrange(headlen):
                temp.append(newstr.pop(0))
                #newstr.pop(0)
                #output.join(str(newstr[i]))
            for i in xrange(group-1,0,-1):
                newstr.insert(i*k,'-')
            
            return output.join(str(e) for e in temp).upper() + '-' + output.join(str(e) for e in newstr).upper()
            






if __name__ == "__main__":
    cls = Solution()
    s = "2-4A0r7-4k" 
    print cls.licenseKeyFormatting(s,3)
    s = "2"
    print cls.licenseKeyFormatting(s,2)
    #print cls.licenseKeyFormatting(s,4)

