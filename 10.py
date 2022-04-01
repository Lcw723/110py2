n,m=map(int,input("輸入N,M的值:").split(" "))
n1=list(map(int,input("輸入矩陣第一列為:").split(" ")))
n2=list(map(int,input("輸入矩陣第二列為:").split(" ")))
for i in range(n):
    for j in range(m):
        print(f"輸出矩陣地{j+1}列:{n1[j]}{n2[j]}")
    break