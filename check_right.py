#input triangle sides and check whether it is a triangle or not.
a=int(input("enter the side of a : "))
b=int(input("enter the side of b : "))
c=int(input("enter the side of c : "))
if a+b>c and a+c>b and b+c>a :
	if a**2+b**2==c**2 :
		print("Right angled triangle.")
	else :
		print("Not a Right angled triangle.")
else :
	print("given sides does not forms a triangle.")
