import sys
from random import randint

def qselect(i,arry):
    
    if arry == [] or i<1 or i >len(arry):
        return None
    else:
    #random.seed()
        pivot_idx = randint(0,len(arry)-1)
        arry[0],arry[pivot_idx] = arry[pivot_idx],arry[0]
        pivot = arry[0]
        left = [x for x in arry if x < pivot]
        right = [x for x in arry[1:] if x >= pivot]
        
        k = len(left)+1
        if k == i:
            return pivot
        elif i < k:
            return qselect(i,left)
        else:
            return qselect(i-k,right)



if __name__ == "__main__":
    t = qselect(6, [11,12, 2,11, 8, 3])
    print t
