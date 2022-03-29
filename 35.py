sA=input("sA:")
sB=input("sB:").split(" ")
sBlist=[]
for i in range(len(sB)):
    sBlist.append(sB[i])


if sA in sBlist:
    print("子字串判斷為:Yes")
else:
    print("子字串判斷為:No")