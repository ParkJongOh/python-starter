def calc(a, b, type):
    if type == 'add':
        return a+b
    elif type == 'sub':
        return a-b

result1 = calc(3,4,'add')
result2 = calc(5,4,'sub')
print(result1)
print(result2)