
def best(n,arr,opt=None):
	if opt == None:
		opt = {0:0}
	collect = []
	for (w,v) in arr:
		if n>=w:
			collect.append(best(n-w,arr,opt) + v)
		else:
			opt[n] = 0
			return opt[n]
	opt[n] = max(collect)
	idx = collect.index(opt[n])
	pick[idx]+=1
	return opt[n],pick

if __name__ == "__main__":
	print best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
