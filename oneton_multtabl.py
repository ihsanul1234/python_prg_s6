#multiplicqtion table of 1-n numbers
n=int(input("Enter the number : "))
for k in range(1,n+1):
	for i in range(1,11):
		print(k,"×",i,"=",k*i)
	print()
