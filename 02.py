e=int(input("請輸入度數:"))
if e<=120:
    print("Summer Month:%.2f"%float(e*2.10))
    print("Non-Summer Month:%.2f"%float(e*2.10))
elif 121<=e<=330:
    print("Summer Month:%.2f"%float(120*2.10+((e-120)*3.02)))
    print("Non-Summer Month:%.2f"%float(120*2.10+((e-120)*2.68)))
elif 331<=e<=500:
    print("Summer Month:%.2f"%float(120*2.10+210*3.02+((e-330)*4.39)))
    print("Non-Summer Month:%.2f"%float(120*2.10+210*2.68+((e-330)*3.61)))
elif 501<=e<=700:
    print("Summer Month:%.2f"%float(120*2.10+210*3.02+170*4.39+((e-500)*4.97)))
    print("Non-Summer Month:%.2f"%float(120*2.10+210*2.68+170*3.61+((e-500)*4.01)))
elif e>=701:
    print("Summer Month:%.2f"%float(120*2.10+210*3.02+170*4.39+e*4.97+((e-700)*5.63)))
    print("Non-Summer Month:%.2f"%float(120*2.10+210*2.68+170*3.61+e*4.01+((e-700)*4.50)))