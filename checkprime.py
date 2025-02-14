#check whether a number is prime or not 
n=int(input("enter the number : "))
i=2
prime="true"
while i<=n//2:
	if n%i==0:
		prime="false"
		break
	i=i+1
if prime=="true":
	print(n," is a prime number.")
else:
	print(n,"is not a prime number.")
