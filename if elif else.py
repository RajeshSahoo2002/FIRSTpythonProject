print("Let's learn if,elif,else in python.")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if (a<b):
    print("i am rajesh")
elif(a>b):
    print("my name is sonu")
else:
    print("Moting")

res=a%2
if(res==0):
    print(a,"is an even number.")
else:
    print(a,"is an odd number.")

x=int(input("Enter the number:"))
res=x%2
if(res==0):
    print(x,"is an Even number.")
    if(x>10):
        print("Good one")
    else:
        print("Hmm bad one.")
else:
    print(x,"is an odd number.")
x=int(input("Enter the value of x:"))
if x==1:
    print(x,"->","One")
elif(x==2):
    print(x,"->","Two")
elif(x==3):
    print(x, "->", "Three")
elif(x==4):
    print(x, "->", "Four")
else:
    print(x, "->", "Five")