decno=int(input("enter the decimal number"))
if decno==0:
	print("equivalent to - 0000")
else:
	binaryno=""
	while decno!=0:
		b=decno%2
		binaryno=str(b)+binaryno
		decno=decno//2
print("the bibary equivalent is ",binaryno)
