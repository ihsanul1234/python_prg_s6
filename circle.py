#python program to find area and circumference of a circle
#standard formula to calculate the area of a circle is : a=pi*r^2
#circumference c = 2*pi*r
import math
r=input("enter the radius : ")
r=int(r) #type conversion
a=math.pi*r*r
c=2*math.pi*r
print("area of the circle is : ",a)
print("circumference of the circle is : ",c)
