def average(scoreList):
    sum = 0
    for i in scoreList:
        sum = sum + i

    average = sum / len(scoreList)
    return average

scoreList = [30,50,70,65,40]

print(average(scoreList))