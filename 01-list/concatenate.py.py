# concatenate all integer from a list to a single number
l1=[1,2,3,4,5,6,7,8,9,10]
s1=''
for x in l1:
    s1 += str(x)
print(int(s1))
