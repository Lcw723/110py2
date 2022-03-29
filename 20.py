a=int(input("組數為:"))
list=[]
for i in range(1,a+1,1):
    a1=input("第%d組:"%i).split(" ")
    b=int(a1[0])
    c=int(a1[1])
    t=250*b+175*c
    print("第",i,"組應收費用:%d"%t)

