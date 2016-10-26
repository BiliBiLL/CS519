import heapq as h

def kmergesort(lst,k):
    if len(lst)<2:
        return lst
    
    result = []
    for i in range(k):
        if len(lst[i::k]) != 0:
            result.append(kmergesort(lst[i::k],k))
    return merge(result)

def merge(m):
    result=[]
    heap=[]
    for i in range(len(m)):
        h.heappush(heap,(m[i][0],i))
        #print heap
    while len(heap) != 0:
        element = h.heappop(heap)

        result.append(element[0])
        h.heappop(m[element[1]])
        if len(m[element[1]]):
            h.heappush(heap,(m[element[1]][0],element[1]))

    return result
