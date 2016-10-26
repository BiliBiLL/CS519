import * from heapq

h = heapq

def kmsort(arry,k):
    length = len(arry)
    heap = []
    if length < 2:
        return arry
    step = length//k
    for i in range(0,length,step):
        heap.append(kmsort(arry[i:i+step],k))
    return merge(heap)


def merge(heap):
    for x in heap:
        
