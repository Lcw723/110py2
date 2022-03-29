ans=input("輸入答案:")
anslist=[]
for i in range(len(ans)):
    anslist.append(ans[i])

while True:
    a=0
    b=0
    yans=input("輸入數字:")
    yanslist=[]
    if yans=="0000":
        print("end")
        break
    for i in range(len(yans)):
        yanslist.append(yans[i])
    
    for i in range(len(yanslist)):
        if yanslist[i]==anslist[i]:
            a+=1
        elif yanslist[i]!=anslist[i] and yanslist[i] in anslist:
            b+=1
    print("%dA%dB"%(a,b))
    if a==4:
        break
    

    

