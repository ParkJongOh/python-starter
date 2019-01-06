def bd(bloodType):
    a = 0
    b = 0
    ab = 0
    o = 0

    for bloodname in bloodType:
        if bloodname == 'A':
            a = a + 1
        elif bloodname == 'B':
            b = b + 1
        elif bloodname == 'AB':
            ab = ab + 1
        elif bloodname == 'O':
            o = o + 1
    return {'A' : a, 'B' : b, 'AB' : ab, 'O' : o}


bloodType = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB', ]
print(bd(bloodType)['A'])

# For문 실행
# if문 실행
