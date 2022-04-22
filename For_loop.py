print("Let's Learn For-Lopp in Python.")
x=["Rajesh",69,19.43,0.098]
for i in x:
    print(i)
y=[10,20,30,40,50,60]
sum=0
for i in y:
    sum=sum+i

print("Sum is ",sum)
s='GOLDMAN SACHS'
for i in s:
    print(i)

for i in range(10):
    print(i)

for i in range(11,21,2):
    print(i)
for i in range (20,10,-1):
    print(i,"Rajesh")
for i in range(0,21):
    if(i%5!=0):
        print(i)
x=int(input("How many candies does the user wants?"))
i=1
while(i<=x):
    print(i,"candy")
    i+=1
print("The nos are:")
for i in range(1,101):
    if(i%3==0 or i%5==0):
        continue
    else:
        print(i)