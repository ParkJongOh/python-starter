def aver(scoreList):
    sum = 0

    for score in scoreList:
        sum = sum + score

    return sum / len(scoreList)

scoreList = [30, 50, 70, 65, 40]
print(aver(scoreList))
# 4. 평균을 내는 함수를 만들어보자
#예약어인 함수와 구분을 잘 하자