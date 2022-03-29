ap=[]
ap.append(["123","456","9000"])
ap.append(["456","789","5000"])
ap.append(["789","888","6000"])
ap.append(["336","558","10000"])
ap.append(["775","666","12000"])
ap.append(["566","221","7000"])

g=int(input('輸入查詢組數N為:'))
for i in range(g):
    sign=input().split(" ")
    for j in range(len(ap)):
        if sign[0]==ap[j][0] and sign[1]==ap[j][1]:
            print(ap[j][2])
            break
        else:
            print("error")
            break