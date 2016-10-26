import sys
import random

def qselect(i,arry):
    if len(arry)== 1:
        return arry[0]

    random.seed()
    pivot = random.choice(arry)
    left = [x for x in arry if x < pivot]
    right = [x for x in arry if x >= pivot]
    
    k = len(left)+1
    if k == i:
        return pivot
    elif i < k:
        return qselect(i,left)
    else:
        return qselect(i-k+1,right)



if __name__ == "__main__":
    t = qselect(3,[4,7,3,1,8,5,9])
    print t
