fruitList = {
    'apple' : {'stock' : 7, 'price' : {'a':3000,'b':2000}},
    'banana' : {'stock' : 10, 'price' : 2500}
}

name = input()

print(fruitList[name]['price']['a'])

#apple의 경우 딕셔너리 안에 또 딕셔너리가 있고 또 딕셔너리가 있지만
#banana의 경우 딕셔너리 안에 딕셔너리 가 있다. print를 할 때 price에 a를 호출하면 apple은 3000이 호출되고 banana는 오류가 발생한다.