from collections import defaultdict
from sys import maxint

def best(n,values):
    back = defaultdict(lambda:None)
    
    def _best(n,opt = defaultdict(lambda:maxint)):
        if n==0:
            opt[n] = 0
            return opt[n]
        if opt[n]!=maxint:
            return opt[n]
        temp = maxint
        for i,vi in enumerate(values):
            if n-vi>=0:
                temp = _best(n-vi,opt)+1
                if temp < opt[n]:
                    opt[n] = temp
                    back[n] = i
        return opt[n]
    return _best(n),backtrace(n,values,back)

def backtrace(n,values,back):
    if back[n] == None:
        return len(values)*[0]
    idx = back[n]
    solution = backtrace(n-values[idx],values,back)
    solution[idx]+=1
    return solution
    
    
if __name__ =="__main__":
    print best(47, [6, 10, 15])
    print best(59, [6, 10, 15])
    print best(37, [4, 6, 15])
    print best(27, [4, 6, 15])
