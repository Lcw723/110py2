doller=int(input("小明身上有幾元:"))
c=input("輸入價格:").split(" ")
clist=[]
a=0
for i in range(len(c)):
    clist.append(c[i]) 

for i in range(len(clist)):
    clist[i]=int(clist[i])
    if clist[i]<=doller:
        a+=1
print(a)
