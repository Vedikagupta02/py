s1="Strawberries"

count={}

for i in s1:
    if i in count:
        count[i]+=1

    else:
        count[i]=1

print(str(count))

