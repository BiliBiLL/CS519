"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 

Example 1:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.

"""

def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row0 = ['q','w','e','r','t','y','u','i','o','p']
        row1 = ['a','s','d','f','g','h','j','k','l']
        row2 = ['z','x','c','v','b','n','m']
        
        final = []
        for word in words:
            res = [True,True,True]
            for x in word:
                res[0] = res[0] and (x.lower() in row0)
                res[1] = res[1] and (x.lower() in row1)
                #print (x.lower() in row1)
                res[2] = res[2] and (x.lower() in row2)
            #print res[0] ,res[1],res[2]
            if res[0] or res[1] or res[2]:
                #print word
                final.append(word)
        return final
        
        
if __name__ == "__main__":
    s = ["Hello", "Alaska", "Dad", "Peace"]
    print findWords(s)
