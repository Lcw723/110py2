c1=int(input("請輸入第1個數字:"))
c2=int(input("請輸入第2個數字:"))
c3=int(input("請輸入第3個數字:"))
c4=int(input("請輸入第4個數字:"))
c5=int(input("請輸入第5個數字:"))
c6=int(input("請輸入第6個數字:"))
c7=int(input("請輸入第7個數字:"))
c8=int(input("請輸入第8個數字:"))
c9=int(input("請輸入第9個數字:"))
c0=int(input("請輸入第10個數字:"))
s=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c0]
s1=sorted(s,reverse=True)
print("最大的3個數字為:",s1[0],",",s1[1],",",s1[2])
print()
print("最小的3個數字為:",s1[7],",",s1[8],",",s1[9])