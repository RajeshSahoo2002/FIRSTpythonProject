print('Dictonary')
dict={1:'Rajesh',2:'Sonu',3:'Kumar',4:'Sahoo',10:'Goldman Sachs'}
print(dict)

#to access a value from a dictionary#
data={10:'Meta',20:'Microsoft',30:'Apple',40:'GoldMan Scahs'}
res=data[30]
print(res) #Means we can only acces the valkues using the keys not the vise-versa#

# In-Built Functions Of Dictionary #
data.clear()
print(data)
#Merging Two List Into a dICTIONARY#
keys=['Rajesh','Aman','Kalinga','Kunal','Sachin','Pritish','Ram']
values=['Python','Cloud','CP','Java','DSA','AI/ML','Blockchain']
serial=[1,2,3,4,5,6,7]
data=zip(serial,keys,values)
print(set(data))

#Deltion In Dictionary
data={'Harsh':'Java','Raj':'JS','Sonal':'C++'}
del data['Raj']
del data['Sonal']
print(data)
# Using List & Dictionary as a value in Dictionary#
print("List Of IDE'S for different languages:")
prog={'Python':['Pycharm','Jupitor','VS Code','IDLE'],'Java':{'JEE':'Netbeans','JSE':'Eclipse'},'JS':['VS Code','Atom','Sublime']}
print(prog)
a=prog['Python']
print(a)
b=prog['Python'][2]
print(b)