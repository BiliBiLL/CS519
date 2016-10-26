import sys
import math
import bisect

def find(l,x,k):
    l.insert(0,-sys.maxint-1)
    l.insert(len(l),sys.maxint)
    index = bisect.bisect(l,x)

    l.insert(index,x)

    left = index - 1
    right = index + 1

    result = []
    for i in range(k):
        if len(l) == k:
            return l
        if abs(l[left] - l[index]) > abs(l[right] - l[index]):
            result.append(l[right])
            right = right + 1
        else:
            result.insert(0, l[left])
            left = left - 1
    return result

if __name__ == "__main__":
    print find([1,2,3,4,4,6,6],5,3)
    print(find([1,2,3,4,4,7], 5.2, 2))
    print(find([1,2,3,4,4,7], 5.2, 3))
    print(find([1,2,3,4,4,7], 5.2, 6))
    print(find([1,2,3,4,4,5,6], 4, 5))    
        
    
        
    
        
            
    
