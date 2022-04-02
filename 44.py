c=int(input(""))
s=[]
b=0
for i in range(c):
    s.append(input(""))
s=list(map(int,s))
for i in range(c-1):
    if s[i+1]>s[i]:
        b=s[i+1]
print(b)
