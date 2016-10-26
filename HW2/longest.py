import sys

def longest(arry):
    [deepth,longpath] = _longest(arry)
    return longpath

def com3(a,b,c):
    max = a if a > b else b
    max = c if c > max else max
    return max

def _longest(tree):
    if tree == None:
        return [0,0]
    if tree == []:
        return [-1,0]
    left,root,right = tree
    print left,root,right
    if left == right == []:
        return [0,0]
    
    [leftdeepth,longpathleft] = _longest(left)
    leftdeepth += 1
    [rightdeepth,longpathright] = _longest(right)
    rightdeepth += 1
    

    deepth = rightdeepth if rightdeepth > leftdeepth else leftdeepth
    sumdeepth = rightdeepth +leftdeepth 
    longpath = com3(sumdeepth,longpathleft,longpathright)
    
    return [deepth,longpath]


if __name__ == "__main__":
    l = longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
    print l
