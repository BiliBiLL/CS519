import sys

def num_inversions(arry):
    [orderlist,num] = _msort(arry)
    return num
def _msort(arry):
    if arry == []:
        return []
    elif len(arry) == 1:
        num = 0
        return [arry,num]
    else:
        mid = len(arry)/2
        left = arry[:mid]
        right = arry[mid:]
        [left,lnum] = _msort(left)
        [right,rnum] = _msort(right)
        #print left,right
        i = 0
        j = 0
        num =0
        orderlist = []
        while i<len(left) and j <len(right):
            if left[i] < right[j]:
                orderlist += [left[i]]
                i+=1
            elif left[i] == right[j]:
                orderlist += [right[j]]
                j+= 1
            else:
                num += 1
                orderlist += [right[j]]
                j+=1

        #print i,j
        if j<len(right):
            orderlist.extend(right[j:])
        if i <len(left):
            orderlist.extend(left[i:])
            offset = len(left) - i
            num += offset*len(right)
        #print left,right
        return [orderlist,num + lnum +rnum]
    

if __name__ == "__main__":
    arry = [4, 1, 3, 2]
    print num_inversions(arry)
