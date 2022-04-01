a=int(input(""))
b=int(input(""))
c=int(input(""))
d=b**2-4*a*c
if d>0:
    ans1=(-b+((b**2-4*a*c)**0.5))/2*a
    ans2=(-b-((b**2-4*a*c)**0.5))/2*a
    print(int(ans1))
    print()
    print(int(ans2))
elif d==0:
    ans3=(-b+((b**2-4*a*c)**0.5))/2*a
    print(int(ans3))
elif d<0:
    print("0")
