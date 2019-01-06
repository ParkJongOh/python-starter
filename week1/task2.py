scoreList = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
result = 0
for score in scoreList:
    sum = sum + score

result = sum / len(scoreList) #들여쓰기 하고 안하고의 차이점은 매번 result값을 확인하는것과 sum 계산을 끝내고 마지막에 하는것의 차이가 있다(들여쓰기 잘못하면 리소스를 많이먹음)
print(result)

#리스트 a를 불러서 합하고 평균을 구하는 문제이다.
#이 문제는 엄청나게 고민을 오래하고 풀었다 처음엔 aver=aver + a[0] 이런식으로 접근을 했다.
#계속 엄청 큰 값이 나와서 고민해보니 aver는 a의 변수인데 거기에 또 a를 하나씩 더하니까 이상한 값이 나온것 같다
#그래서 sum = 0으로 만들고 sum에 aver를 더하니까 a의 합한값이 잘 나왔다.
#len 함수를 처음으로 이용해 보았다.