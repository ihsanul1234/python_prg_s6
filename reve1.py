rev=0
print("enter the number")
num=int(input())
while num!=0:
	d=num%10
	rev=rev*10+d
	num=num//10
print("reverse is ",rev)
