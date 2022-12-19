f=open('./dataset1.txt','r')
data={}
features=f.readline()
for i in features.split():
    data[i]=[]
keys=list(data.keys())
values = f.readlines()
no_of_val=0
for i in values:
    k=0
    no_of_val=no_of_val+1
    for j in i.split():
        data[keys[k]].append(j)
        k=k+1
print("enter the nominal attributes:")
nom_a=list(map(str,input().split()))
print("enter the numeric attributes:")
num_a=list(map(str,input().split()))
disnom=[[0 for x in range(no_of_val)] for x in range(no_of_val)]
disnum=[[0 for x in range(no_of_val)] for x in range(no_of_val)]
simnom=[[0 for x in range(no_of_val)] for x in range(no_of_val)]
for i in range(no_of_val):
    for j in range(i):
        m=0
        e_dist=0
        for k in nom_a:
            if data[k][i]==data[k][j]:
                m=m+1
        for k in num_a:
            e_dist=e_dist+((float(data[k][i])-float(data[k][j]))**2)
            disnom[i][j]=(len(nom_a)-m)/len(nom_a)
            disnum[i][j]=round(e_dist**0.5,2)
            simnom[i][j]=1-disnom[i][j]
print("the dissimilarity matrix for nominal attributes is:")
for i in range(no_of_val):
    for j in range(no_of_val):
        if j>i:
            print(" ",end=' ')
        else:
            print(disnom[i][j]," ",end=' ')
    print()
print("the similarity matrix for nominal attributes is:")
for i in range(no_of_val):
    for j in range(no_of_val):
        if j>i:
            print(" ",end=' ')
        else:
            print(simnom[i][j]," ",end=' ')
    print()
print("the dissimilarity matrix for numeric attributes is:")
for i in range(no_of_val):
    for j in range(no_of_val):
        if j>i:
            print(" ",end=' ')
        else:
            print(disnum[i][j]," ",end=' ')
    print()

