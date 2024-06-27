print("My name is Vedika.")

name="Vedika"
age=20

print("My name is ", name)
print("My age is ",age)

age2=age
print(age2)

name1="skm"
name2='skm'
name3='''skm'''

name="vedika"
age=20
salary=90.00
old=True 
x2=None

print(type(name))
print(type(age))
print(type(salary))
print(type(old))
print(type(x2))

a=9
b=6
sum=a+b
print(sum)

a=2
b=3
text="@"

print(a*text*b)

a="2"
b=3
text="@"

print((a+text)*b)

a=2
b=3
c=5
print(a+b*c)

a=9.0
b=3
print(a*b)

a=3
b=5
c=a/b
d=a//b
print(c)
print(d)

a=12
b=5
print(a//b)

a=-12
b=5
print(a//b)

a=5
b=2
print(a%b)

a=5
b=-2
print(a%b)

name=input("Enter name: ")
age=int(input("Enter age: "))
price=float(input("Enter Price: "))

print("My name is",name, "and I am " ,age ,"years old")

print("the price of tomatoes is ", price)

marks=int(input("Enter marks: "))

if (marks>=90):
    print("A")
    
elif (marks>=80 and marks<90):
    print("B")
    
elif(marks>=70 and marks<80):
    print("C")
    
else:
    print("D")
    
food=input("Enter food: ")
print("sweet ") if food=="cake" or food=="rasgolla" else print("not sweet")
eat="yes " if food=="cake " else "no"
print(eat)

age=int(input("Enter age: "))
vote=("yes", "no") [age<18]
print(vote)

p=float(input("Enter num: "))
r=float(input("Enter num: "))
t=float(input("Enter num: "))

si=p*r*t/100
print(si)

a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

print(a==b)
print(a!=b)
print(a>b)
print(a<b)

num=10
num%=10
print(num)

a=10
b=9.9
sum=a+b
print(sum)

a=80
b=int("7")
sum=a+b
print(sum)

a=9.78
b=str(a)
print(b)
print(type(b))

num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
sum=num1+num2
print(sum )

#ques2: print average 
#ques3: lesser and greater
#ques4: area of square
