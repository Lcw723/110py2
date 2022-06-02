a=list(input("請輸入string_a:"))
b=list(input("請輸入string_b:"))
l1=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            if a[i] not in l1:
                l1.append(a[i])

l1.sort()
s=""
if len(l1)>0:
    for i in range(len(l1)):
        s+=l1[i]
    print(s)
else:
    print("N")
