from collections import defaultdict
from heapq import heappop,heappush

def match(a,b):
    m = a+b
    if m=="AU" or m=="UA" or m=="CG" or m=="GC" or m=="GU" or m=="UG":
        return True
    else:
        return False

def backtrace(l,r,back,seq,rna):
    if back[l,r][0] == True:
        seq[l] = '('
        seq[r-1] = ')'
        backtrace(l+1,r-1,back,seq,rna)
    else:
        k = back[l,r][1]
        if k!= -1:
            backtrace(l,k,back,seq,rna)
            backtrace(k,r,back,seq,rna)

def best(rna):
    opt = defaultdict(lambda:-1)
    back = defaultdict(lambda:(False,-1))

    def helper(l,r,opt,back):
        if l+1 == r:
            opt[l,r]=0
            return opt[l,r]
        if l==r:
            opt[l,r]=0
            return opt[l,r]
        if opt[l,r] != -1:
            return opt[l,r]
        else:
            maxval = 0
            if match(rna[l],rna[r-1]):
                maxval = helper(l+1,r-1,opt,back) + 1
                back[l,r] = (True,l)

            for k in range(l+1,r):
                opt[l,r] = helper(l,k,opt,back) + helper(k,r,opt,back)
                if maxval< opt[l,r]:
                    maxval = opt[l,r]
                    back[l,r] = (False,k)
            opt[l,r] = maxval
            return opt[l,r]

    
    length = len(rna)
    bestval = helper(0,length,opt,back)
    seq = length*['.']
    backtrace(0,length,back,seq,rna)
    st = ""
    for i in seq:
        st+=str(i)
    return bestval,st


def total(rna):
    tot = defaultdict(int)
    length = len(rna)
##    for i in xrange(length):
##        tot[i,i+1] = 1
##        tot[i,i] = 1
    def helper(l,r,tot):
        if l==r-1:
            tot[l,r] = 1
            return tot[l,r]
        if l==r:
            tot[l,r] = 1
            return tot[l,r]
        if tot[l,r]!=0:
            return tot[l,r]
        else:
            tot[l,r] += helper(l+1,r,tot)
            for k in range(l+1,r+1):
                if match(rna[l],rna[k-1]):
                    tot[l,r] += helper(l+1,k-1,tot)*helper(k,r,tot)
            return tot[l,r]

    return helper(0,length,tot)


def kbest(rna,n):
    length = len(rna)
    opt = defaultdict(list)
    def helper(l,r,opt):
        if l==r or l==r-1:
            opt[l,r] = 0
            return opt[l,r]
        else:
            



    def tryadd(split,index1,index2):
        if index1<len(opt[i,split]) and index2<len(opt[split,j]) \ 
           and not (split,index1,index2) in used:
               used.add((split,index1,index2))
               heappush(heap,(-opt[i,split][index1][0]-opt[split,j][index2][0]-1,\
                        split,index1,index2))

    for k in xrange(l+1,r+1):
        if match(rna[l],rna[k-1]):
            trypush(k,0,0)
    for _ in xrange(l+1,r+1):
        val,split,idx1,idx2 = heappop(heap)
        trypush(split,idx1+1,idx2)
        trypush(split,idx1,idx2+1)
        
    for _ range(n):
        nomatch = helper(l+1,r)
        nomatch.reverse()
        nbst = heappop(heap)
        if nomatch[-1] > :
            opt[l,r].append(nomatch.pop())
        else:
            
        heappush(h,heappop(heap))
        
        

if __name__ == "__main__":
    print best("UUCAGGA")
    print total("UUCAGGA")
    print total("ACAGU")
    print total("AUAU")
##    print best("GUUAGAGUCU")
##    print best("GCACG")
##    print best("AUAACCUUAUAGGGCUCUG")
##    print best("UUGGACUUGAGAAAAG")
##    print best("UCAAUGGGUAGUAAAU")
##    print best("UUUGGCACUUUCAGA")
##    print best("ACACACCUUGUCCGUGAA")
##    print best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG")
##    print best("CGCGAAUAAAAAGGCACUGUU")
##    print best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC")
##    print best("UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU")
##    print best("AUACGUCGGGGACAAGAAUUACGG")
##    print best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")
##    print best("CGAGGUGGCACUGACCAAACACCACCGAAAC")
##    print best("CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU")
##    print best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")
##    print best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")

