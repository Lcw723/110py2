from ast import While


m=int(input("請輸入階乘值M:"))
h=0
n=1
while True:
    h+=1
    n*=h
    if n>m:
        print("超過M為%d的最小階層N為%d"%(m,h))
        break

