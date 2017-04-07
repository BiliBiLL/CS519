"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:

    The name of a file contains at least a . and an extension.
    The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""



class Solution(object):
    def lengthLongestPath(self, ip):
        """
        :type input: str
        :rtype: int
        """
        def splitline(s):
            a = []
            i=0       
            while i< len(s):
                temp = []               
                while i<len(s) and s[i] != '\n':                    
                    temp.append(s[i])
                    i+=1                    
                a.append(temp)
                i+=1
            return a
            
        pathline = {0:0}
        
        sl = splitline(ip)
        longest = 0
        for x in sl:
            print len(x),x
            depth = 0
            for t in x:
                if t == '\t':depth += 1
            if '.' in x:
                longest = max(longest,pathline[depth] + len(x) - depth)
            else:
                pathline[depth + 1] = pathline[depth] + len(x) + 1 - depth
            print depth
            #print pathline[depth]
        return longest
                    
if __name__ == "__main__":
    s1="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    s2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    l = Solution()
    print l.lengthLongestPath(s1)            
    print l.lengthLongestPath(s2)
    
                    
                    
"""Note:  
1."while s[i] != '\n' and i<len(s):" this statement in python is execute in sequence, it will check the condition "s[i]!='\n'" then "i<len(s)", so it will cause KeyError problem, the key i will out of range when check for the condition s[i].
2.debugging is a very good habit to find out the problems, don't hesitate to do that, rahter than just sit here and "guess", set some break point and see different result will be more helpful.
This problem is very tricky, but worth to do.
"""                  
