n=int(input("輸入比數n:"))
enandch={}
for i in range(n):
    en,ch=input(" ").split(" ")
    enandch[en]=ch
ew=input("輸入欲查詢單字:")

print(ew,"中文意思為",enandch[ew])