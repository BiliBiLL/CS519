import sys

def msort(arry):
    if arry == []:
        return []
    elif len(arry) == 1:
        return arry
    else:
        mid = len(arry)/2
        left = arry[:mid]
        right = arry[mid:]
        left = msort(left)
        right = msort(right)
        #print left,right
        i = 0
        j = 0
        orderlist = []
        while i<len(left) and j <len(right):
            if left[i] < right[j]:
                orderlist += [left[i]]
                i+=1
            else:
                orderlist += [right[j]]
                j+=1

        #print i,j
        if j<len(right):
            orderlist.extend(right[j:])
        if i <len(left):
            orderlist.extend(left[i:])
        #print left,right
        return orderlist
    

if __name__ == "__main__":
    arry = [4,7,2,1,3,8,5]
    print msort(arry)
    
