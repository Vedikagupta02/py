import keyword

#keyword module to see all the keywords in python version

print(keyword.kwlist)
print(len(keyword.kwlist))

#taking input from user 

value=input("enter value: ")
print(value)
print(type(value))

value=input("Enter value: ")

print(value, sep='#',end='%')

print(1,2,3,sep='#',end='$')

sample_file=open("C:/Users\VEDIKA\OneDrive/Desktop/py/input.txt", "w")
print(1,2,3,sep='#',end='$',file=sample_file)

print("Hello to all {} people in class".format(10))

str1=int(input("Enter the number of people to greet"))

print("Greeting to all {} people present here".format(str1))

num1=10
num2=90

print(num1+num2)

str1="hello "
str2="good evening"

print(str1+str2)

num1=90
str1="hello"

print(str(num1)+str1)

num1=10
print(type(num1))
num2=6.7
print(type(num2))
num3=5+2j
print(type(num3))

print(0b101)
print(0o156)
print(0xAFB)

print(10+15.14)

val=int(16.77)
print(val)
val2=complex("20+11j")
print(val2)
print(type(val2))

import random

print(random.randrange(20,50))

print(random.random())

list1=["hi","my","bye","say","tea"]

print(random.choice(list1))

random.shuffle(list1)
print(list1)

import math as mt

print(mt.pi)
print(mt.factorial(5))
print(mt.pow(2,4))

list1=["hello","bye",1,2,3,4,True,False]
print(list1[0])
print(list1[-1])

list1[-1]="GO"
print(list1)

tup1=("hello","bye",1,2,3,4,True,False)
print(tup1[0])
print(tup1[-1])

tup1[-1]="GO"
print(tup1)



dict1={"Name":"Vedika","Age":20, "Favrouite":"Coco" , "Houseno":9}

print(dict1["Name"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1["Age"]=19
print(dict1)

set1={1,1,1,2,3,4,4,4,4,5}
print(set1)