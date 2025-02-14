#sum of cube of all even numbers <= to the given integer
sum=0
n=int(input("Enter a positive integer :"))
for i in range(n+1):
 if i>0 :
  if i%2==0:
   sum=sum+i**3
print("sum of cube of all integers until ",n,"is ",sum)
