n=int(input("整數n:"))
n1=n
cl=[]
while True:
    if n==1:
        break
    else:
        if n%2==0:
            n/=2
            cl.append(n)
        else:
            n=3*n+1
            cl.append(n)
print(n1)
for i in cl:
    print(round(i),end=" ")
    