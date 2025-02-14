#sum of a number
sum=0
n=int(input("enter the number : "))
t=n
while n!=0 :
	sum=sum+n%10
	n=n//10
print("the sum of ",t,"is ",sum)
