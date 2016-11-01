def lis(arr):
	L = 0
	for i in range 0 to N-1:

	lo = 1
	hi = L
	while lo ≤ hi:
	mid = ceil((lo+hi)/2)
	if X[M[mid]] < X[i]:
		lo = mid+1
	else:
		hi = mid-1