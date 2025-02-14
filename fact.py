def myfun(n):
	n=int(input("enyer the numvet"))
	if n==0:
		return 1
	else:
		return n*fact(n-1)
	print(fact(n))
