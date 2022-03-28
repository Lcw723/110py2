a=input("輸入值為:").split(",")
min0=''
max0=''
value_int=list(map(int,a))   
value_int.sort()
value_int=list(map(str,value_int))
for i in range(len(a)):
    min0+=value_int[i]

value_int=list(map(int,a))
value_int.reverse()
value_int=list(map(str,value_int))
for i in range(len(a)):
    max0+=value_int[i]

print("最大數列值與最小數列值差值為:%d"%(int(max0)-int(min0)))