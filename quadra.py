#input points and find the quadrant
x=int(input("enter the value of x : "))
y=int(input("enter the value of y : "))
if x>0 and y>0:
	print("first quadrant.")
elif x<0 and y>0:
	print("second quadrant.")
elif x<0 and y<0:
	print("third quadrant.")
elif x>0 and y<0:
	print("fourth quadrant.")
else :
 print("point is at origin.")
