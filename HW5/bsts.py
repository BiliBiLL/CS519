

def bstsrec(n):
    if n ==0:
        return 1
    sum = 0
    for i in xrange(0,n):
        sum += bstsrec(i) * bstsrec(n-i-1)
    return sum

def bsts(n):
    cache = [1]+[0]*n
    for i in range(1,n+1):
        for j in range(1,i+1):
            #print i,j-1,i-j
            cache[i]+=cache[j-1]*cache[i-j]         
    return cache[n]

if __name__ == "__main__":
    print bstsrec(7)
    print bsts(7)
