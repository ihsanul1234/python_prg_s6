psum=0
nsum=0
pc=0
nc=0
print("enter the num :")
for i in range(4):
	num=int(input())
	if num>0:
		psum+=num
		pc+=1
	else:
		nsum+=num
		nc+=1
print("sum of positive num : ",psum)
if pc!=0:
	print("avg of +ve num:",psum/pc)
if nc!=0:
	print("avg of -ve num : ",nsum/nc)

