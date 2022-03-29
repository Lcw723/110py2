from numpy import ones
while True:
    cstr=input("檢測的字元(end結束)")
    if cstr=="end":
        print("檢測結束")
        break
    else:
        clist=[]
        appear=0
        one=input("檢測的單一字元:")
        for i in range(len(cstr)):
            clist.append(cstr[i])
        for i in range(len(clist)):
            if one==clist[i]:
                appear+=1
        print("字元",one,"總共出現",appear,"次")