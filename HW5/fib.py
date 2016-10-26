import time

def recfib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return recfib(n-1)+recfib(n-2)

def memofib(n,cache=[0,1]):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n<=len(cache):
        return cache[n-1]
    else:
        cache += [memofib(n-1) + memofib(n-2)]
        return cache[-1]

if __name__ == "__main__":
    for n in xrange(5,37):
        starttime = time.time()
        print n,recfib(n),time.time()-starttime

    for n in xrange(5,37):
        starttime = time.time()
        print n,memofib(n),time.time()-starttime
