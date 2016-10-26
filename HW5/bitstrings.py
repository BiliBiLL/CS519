def num_yes(n,a = None):
    return 1 if n == 0
    return 2 if n == 1
        
    a[n] = a[n-1] if a[n] == 1 else a[n-2]
    return
