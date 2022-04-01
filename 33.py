subject=["國文","英文","微積分","體育","程式設計"]
score=[]
total=0
avg=0

score.append(int(input("國文:")))
score.append(int(input("英文:")))
score.append(int(input("微積分:")))
score.append(int(input("體育:")))
score.append(int(input("程式設計:")))

for i in range(len(score)):
    total+=score[i]

avg=total/len(score)
print("平均分數:%.2f"%avg)
score.sort()
print()
print(f"最高分科目:{subject[4]}{score[4]}分")
print()
print(f"最低分科目:{subject[0]}{score[0]}分")
