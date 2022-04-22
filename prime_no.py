print("Let's learn to write prime no in python:")
import math as m
x=int(input("Enter the the no:"))
res=int(m.sqrt(x))
a=0
for i in range(2,res+1):
    if(x%i==0):
        a=1
        break

if(a==0):
    print(x,'is a prime number.')
else:
    print(x,'is not a prime number')

for i in range(3):
    for j in range(3):
        print("# ",end="")
    print()
for i in range(4):
    for j in range(i+1):
        print("GS ",end="")
    print()
for i in range(4):
    for j in range(4-i):
        print("Rajesh ",end="")
    print()
for i in range(4):
    for j in range(4-i):
        print(j+1,end="")
    print()
