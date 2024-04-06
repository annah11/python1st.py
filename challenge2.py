# checking and removing if there is any duplicate in a list
l1=[3,5,6,8,4,7,6,3,6,10]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)