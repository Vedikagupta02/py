# import keyword

# #keyword module to see all the keywords in python version

# print(keyword.kwlist)
# print(len(keyword.kwlist))

# #taking input from user 

# value=input("enter value: ")
# print(value)
# print(type(value))

# value=input("Enter value: ")

# print(value, sep='#',end='%')

# print(1,2,3,sep='#',end='$')

sample_file=open("C:/Users\VEDIKA\OneDrive/Desktop/py/input.txt", "w")
print(1,2,3,sep='#',end='$',file=sample_file)