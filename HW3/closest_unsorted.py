import sys
import math
from random import *


def qselect(arry,i):
    
    if arry == [] or i<1 or i >len(arry):
        return None
    else:
        pivot_idx = randint(0,len(arry)-1)
        #arry[0],arry[pivot_idx] = arry[pivot_idx],arry[0]
        pivot = arry[pivot_idx]
        left = [x for x in arry if x < pivot]
        right = [x for x in arry if x > pivot]
        mid = [x for x in arry if x == pivot]
        
        k = len(left)
        h = len(mid)
        return left + mid[:i-k] if  k < i and i <= k+h else \
            qselect(left,i) if i <= k else\
            qselect(right,i-k-h)


def find(arry,x,k):
    offset = [abs(s - x) for s in arry]
    return qselect(offset,k)

if __name__ == "__main__":
    result = find([4,1,3,2,7,4], 5.2, 3)
    print result
