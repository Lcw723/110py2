st=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
en=set(['John','Mary','Fiona','Claire','Ben','Bill'])
mt=set(['Mary','Fiona','Claire','Eva','Ben'])
print("英文與數學都及格:",en&mt)
print("數學不及格:",mt^st)
print("英文及格且數學不及格:",en&(mt^st))