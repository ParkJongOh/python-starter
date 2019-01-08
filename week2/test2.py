def bloodList(bloodType):
    a = 0
    b = 0
    ab = 0
    o = 0
    for blood in bloodType:
        if blood == 'A':
            a += 1
        elif blood == 'B':
            b += 1
        elif blood == 'AB':
            ab += 1
        elif blood == 'O':
            o += 1
    return{'A' : a, 'B' : b, 'AB' : ab, 'O' : o}


bloodType = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB', ]
print(bloodList(bloodType)['A'])
# 2. 혈액형 리스트자료형을 넘겨주면 각 딕셔너리 형태로 각 혈앵형 개수를 넘겨주는 함수
