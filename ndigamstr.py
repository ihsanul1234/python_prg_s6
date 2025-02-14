#check whether a given ndigit number is amstrong or not
num=int(input("Enter a n-digit number : "))
order=len(str(num))
sum=0
temp=num
while temp>0:
        digit=temp%10
        sum+=digit**order
        temp=temp//10
if num==sum:
        print(num," is an amstrong number")
else :
        print(num,"is not an amstrong number.")
