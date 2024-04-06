# overlaping elements of two lists
l1=[1,2,3,4,5]
l2=[1,3,5,7,9]
l3=[]
for i in  l1:
    if i in l2:
        l3.append(i)
print(l3)
