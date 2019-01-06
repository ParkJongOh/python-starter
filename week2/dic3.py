fruitList = {
    'apple' : {'stock' : 7, 'price' : {'a':3000,'b':2000}},
    'banana' : {'stock' : 10, 'price' : 2500}
}

name = input()

print(fruitList[name]['price'])