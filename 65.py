a1=input("請輸入A的好友:").split()
b1=input("請輸入B的好友:").split()

f=0
for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i]==b1[j]:
            f+=1

print(f)