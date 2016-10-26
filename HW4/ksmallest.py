import heapq as h

def ksmallest(k, l):
    if l == []:
        return l
    result = []
    for i in l:
        if len(result) < k:
            h.heappush(result, -i)#-i
        elif -result[0] > i:#-result
            h.heappushpop(result, -i)#-i
    return [-i for i in result]#-i
