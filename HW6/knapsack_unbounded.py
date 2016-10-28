def best1(n,arr):
    opt = {0:0}
    if n<=0:
        return 0
    collect = []
    for (w,v) in arr:
        if n-w <0:
            opt[n] = 0
            return opt[n]
        collect.append(best1(n-w,arr) + v)
    opt[n] = max(collect)
    return opt[n]


if __name__ == "__main__":
    print best1(3, [(2, 4), (3, 5)])
    print best1(3, [(1, 5), (1, 5)])
    print best1(3, [(1, 2), (2, 5)])
    print best1(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
    print best1(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
