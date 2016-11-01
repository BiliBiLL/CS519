def best(n,arr):
	opt = {}
	count = {}
	dim = len(arr)
	for i in range(n+1):
		opt[i] = [0 for j in range(dim)]

	for i in range(n+1):
		count[i] = [0 for j in range(dim)]
	val = _best(n,arr,opt,dim-1,count)
	print val,backtrace(n,arr,count)

def backtrace(n,arr,count):
	i = n
	res = []
	for idx in range(len(arr)-1,-1,-1):
		c = count[i][idx]
		w = arr[idx][0]
		res.append(c)
		i-=w*c
	res.reverse()
	return res

def _best(n,arr,dp,idx,count):
	if n<=0 or idx<0:
		return 0
	if dp[n][idx]!=0:
		return dp[n][idx]

	w,v,c = arr[idx]
	maxx = 0
	maxj = 0
	best_v =0
	for j in range(c+1):
		if n - w*j >= 0:
			best_v =_best(n - w*j ,arr,dp,idx-1,count) + v*j
			if best_v > maxx:
				maxx = best_v
				maxj = j
	dp[n][idx] = maxx
	count[n][idx] = maxj
	return dp[n][idx]



if __name__ =="__main__":
	best(3, [(1, 5, 2), (1, 5, 3)])
	best(3, [(1, 5, 1), (1, 5, 3)])
	best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
	best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])