#find the sum of even numbers from given numbers
sum=0
n=int(input("enter the numbers of numbers : "))
print("enter the numbers : ")
for i in range(n):
	num=int(input())
	if num%2==0:
		sum=sum+num
print("the sum of given numbers : ",sum)
