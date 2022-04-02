n=int(input("輸入比數n:"))
award={}
for i in range(n):
    a,value=input(" ").split(" ")
    award[a]=value
for a,value in award.items():
    print("%s牌得到%s面"%(a,value))
