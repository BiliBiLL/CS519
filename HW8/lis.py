##def lis(arr):
##    def helper(arr):
##        if arr == None:return 0
##        opt = [1]*len(arr)
##        for i,val in enumerate(arr):
##            for j in range(i):
##                if arr[j] < arr[i]:
##                    opt[i] = max(opt[j]+1,opt[i])
##        return opt
##
##    def backtrace(opt,biggest):
##        res = []
##        
##        res.reverse()
##        return res
##        
##    ans = helper(arr)
##    return backtrace(ans,max(ans))




from collections import defaultdict

def lis(seq):
    dp = defaultdict(int)
    opt=0
    back = defaultdict(lambda:-1)
    best_idx = -1
    for i,item in enumerate(seq):
        max_pre = 0
        for j in range(i):
            if seq[j] < item and dp[j]>max_pre:
                max_pre = dp[j]
                back[i] = j
        dp[i] = max_pre +1
        if opt < dp[i]:
            opt = dp[i]
            best_idx = i
    return _backtrack(seq,back,best_idx)

def _backtrack(seq,back,best_idx):
    i = best_idx
    p = back[i]
    res = ""+seq[best_idx]
    while p>=0:
        res+=seq[p]
        p=back[p]
    res=res[::-1]
    return res




