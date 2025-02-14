print("prime less than 1000")
for n in range(2,1000):
	i=2
	while i<=n/2:
		if n%2==0:
			break
		i+=1
	else:
		print(n,end=' ')
