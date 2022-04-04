n=int(input("輸入n值:"))
ne={}
for i in range(n):
    n=input("請輸入姓名:")
    e=input("請輸入電子郵件:")
    ne[n]=e
w=input("請輸入要查詢電子郵件的姓名:")
print(w,"電子郵件帳號為",ne[w])
