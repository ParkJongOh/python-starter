
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
num = len(a)
sum = 0
i = 0
for b in a:
    sum = sum + b
    i = sum / num
print (i)

#리스트 a를 불러서 합하고 평균을 구하는 문제이다.
#이 문제는 엄청나게 고민을 오래하고 풀었다 처음엔 aver=aver + a[0] 이런식으로 접근을 했다.
#계속 엄청 큰 값이 나와서 고민해보니 aver는 a의 변수인데 거기에 또 a를 하나씩 더하니까 이상한 값이 나온것 같다
#그래서 sum = 0으로 만들고 sum에 aver를 더하니까 a의 합한값이 잘 나왔다.
#len 함수를 처음으로 이용해 보았다.