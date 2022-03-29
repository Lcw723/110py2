a=input("輸入月租費及通話時間為:").split(",")
b=int(a[0])
c=int(a[1])
if b==186:
    if (c*0.09)<=(186):
        print("通話費為:%d"%round(c*0.09*0.9))
    elif (c*0.09)>(186*2):
        print("通話費為:%d"%round(c*0.09*0.8))
elif b==386:
    if (c*0.08)<=(386):
        print("通話費為:%d"%round(c*0.08*0.8))
    elif (c*0.08)>(386*2):
        print("通話費為:%d"%round(c*0.08*0.7))
elif b==586:
    if (c*0.07)<=(586):
        print("通話費為:%d"%round(c*0.07*0.7))
    elif (c*0.07)>(586*2):
        print("通話費為:%d"%round(c*0.07*0.6))
elif b==986:
    if (c*0.06)<=(986):
        print("通話費為:%d"%round(c*0.06*0.6))
    elif (c*0.06)>(986*2):
        print("通話費為:%d"%round(c*0.06*0.5))