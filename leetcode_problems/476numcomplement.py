

def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        l = len(bin(num)) - 2
        whole = 0
        for i in xrange(l):
            whole += pow(2,i)

        res = whole - num
        return res
        
if __name__ == "__main__":
    num = 5
    print findComplement(num)
    num = 1
    print findComplement(num)



    
