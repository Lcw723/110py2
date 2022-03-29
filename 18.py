num=input("輸入數字:").split(" ")
A,J,Q,K=1,11,12,13
sum=0
for j in range(len(num)):
    if num[j]=="J":
        num.remove("J")
        num.insert(j,11)

    elif num[j]=="Q":
        num.remove("Q")
        num.insert(j,12)

    elif num[j]=="K":
        num.remove("K")
        num.insert(j,13)

    elif num[j]=="A":
        num.remove("A")
        num.insert(j,1)
    num[j]=int(num[j])
    sum+=num[j]
print(sum)
