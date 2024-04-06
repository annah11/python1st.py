# minimum index sum of two lists
fav1=['pizza','nuggets','hotdog','cheese','pasta']
fav2=['cheese','pizza','nuggets','pasta','hotdog']
index1=10
index2=10
for i in range(len(fav1)):
    indx=fav2.index(fav1[i])
    if i +indx< index1+index2:
        index1=i
        index2=index1
print(fav1[index1],index1+index2)
