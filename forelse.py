print("Let's learn For else in Python:")
nums=[18,32,47,56,23]
for i in nums:
    if(i%5==0):
        print(i,end="")
        break
    else:
        print("NOT FOUND")

# Using For else concept in python #
for i in nums:
    if(i%5==0):
        print(i)
        break
else:
    print("not found")