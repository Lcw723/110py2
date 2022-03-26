def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

num=input("請輸入正整數:")
a=[]
for i in range(len(num)):
    for j in range(i,len(num)):
        key=int(num[i:j+1])
        prime(key)
        if prime(key):
            a.append(key)
if len(a)>0:
    print(f"子字串中最大的質數值為:{max(a)}")
else:
    print("No prime found")