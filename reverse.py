#reverse of a number.
rev=0
num=int(input("Enter the number : "))
while num!=0:
 d=num%10
 rev=rev*10+d
 num=num//10
print("the reversed output : ",rev)
