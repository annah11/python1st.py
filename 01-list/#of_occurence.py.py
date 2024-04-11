# find the number of occurences of each item
h1=['A', 'B','C','D','E','F','A','B','C','B','E']
result=[]
for item in h1:
    if item not in result:
        result.append(item)
        count=h1.count(item)
        result.append(count)

print(result)