#find the sum and average of 4 positive inputed numbers 
psum=0
nsum=0
pc=0
nc=0
print("enter the +ve and -ve numbers : ")
for i in range(4):
 n=int(input())
 if n>0:
  psum=psum+n
  pc=pc+1
 else:
  nsum=nsum+n
  nc=nc+1
print("the sum of positive numbers is ",psum)
if pc!=0:
 print("The average of positive no., : ",psum/pc)
print("the s of negative no., : ",nsum)
if nc!=0:
 print("The average of negative no., : ",nsum/nc)
