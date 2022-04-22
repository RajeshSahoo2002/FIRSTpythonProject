print("Fibbonacci Numbers")
a,b,sum=0,1,0
print("a =",a,",","b=",b)
n=int(input("Enter the value of n:"))
for i in range(1,n):
    sum=a+b
    print("Sum is ",sum)
    a=b
    b=sum
print("New value a =",a,",","New value of b=",b)