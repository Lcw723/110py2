money=int(input("請輸入金額:"))
total=0
while True:
    if money==0:
        break
    else:
        if money-100>=0:
            total+=1
            money-=100
        else:
            if money-50>=0:
                total+=1
                money-=50
            else:
                if money-10>=0:
                    total+=1
                    money-=10
                else:
                    if money-5>=0:
                        total+=1
                        money-=5
                    else:
                        if money-1>=0:
                            total+=1
                            money-=1
print(total)
        