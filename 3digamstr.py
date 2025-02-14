#check whether a given  number is amstrong or not
num=int(input("Enter a 3digit number : "))
sum=0
temp=num
while temp>0:
	digit=temp%10
	sum+=digit**3
	temp=temp//10
if num==sum:
	print(num," is an amstrong number")
else :
	print(num,"is not an amstrong number.")
