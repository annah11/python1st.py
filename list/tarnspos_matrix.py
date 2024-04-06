l1=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
l2=[]
for i in range(4):
    m=[]
    for j in range(3):
        m.append(l1[j][i])
    l2.append(m)
print(l2)