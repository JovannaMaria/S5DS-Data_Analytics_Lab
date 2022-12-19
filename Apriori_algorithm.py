from tabulate import tabulate
f=open('./dataset_apriori.txt','r')
d={}
header=f.readline().split()
l2=[]
tab=[]
for i in f.readlines():
    l=i.split()
    j=l[0]
    l.remove(j)
    t=[j]
    t.append(l)
    tab.append(t)
    d[j]=l
    l2.extend(l)
s1=set(l2)
l2=list(s1)
l2.sort()
print("the given dataset is:")
print(tabulate(tab,headers=header,tablefmt="mixed_grid"))
min_sup=2
n=0
while(len(l2)>0):
    l1={}
    for item in l2:
        it=item.split()
        it=set(it)
        x=list(it)
        x.sort()
        item=""
        for k in range(len(x)):
            item=item+x[k]+" "
        count=0
        for tr in d:
            d[tr]=set(d[tr])
            if(it.issubset(d[tr])):
                count=count+1
        if(count>=min_sup):
            l1.update({item:count})
    n=n+1
    print("\nL",n)
    header=[str(n)+" itemset","support"]
    tab=[]
    for i in l1:
    	t=[i,l1[i]]
    	tab.append(t)
    print(tabulate(tab,headers=header,tablefmt="mixed_grid"))
    l1=list(l1.keys())
    for i in range(len(l1)):
        l1[i]=[l1[i]]
    l2=[]
    
    for i in l1:
        for j in l1:

            if(len(i)==1):
                flag =0
                if(n>1):
                    l=i[0].split()
                    m=j[0].split()
                    for k in range(len(l)-1):
                        if(l[k]!=m[k]):
                            flag=1
                            break
                if(flag==0 and i<j):
                    c2=""
                    c2=c2+i[0]+" "+j[0]
                    l2.append(c2)
    l2.sort()
