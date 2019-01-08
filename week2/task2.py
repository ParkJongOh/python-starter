def blooding(bloodType):
    a = 0
    b = 0
    ab = 0
    o = 0
    for blood in bloodType:
        if blood == 'A':
            a+=1
        elif blood == 'B':
            b+=1
        elif blood == 'AB':
            ab+=1
        elif blood == 'O':
            o+=1
    return{'A' : a, 'B' : b, 'AB' : ab, 'O' : o}  #들여쓰기를 잘못하면 for문을 다 실행하고 리턴하는게 아니라 한번 실행하고 리턴함.


bloodType = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB', ]
print(blooding(bloodType))


#2. 혈액형 리스트자료형을 넘겨주면 각 딕셔너리 형태로 각 혈앵형 개수를 넘겨주는 함수
#먼저 함수를 예약한다. 함수의 이름은 blooding 으로 하였고 bloodType를 매개변수 라고 하였다.
#매개변수 bloodType으로 리스트를 입력받았고 for문을 통하여 반복하였다. if문을 통하여 list를 반복하여 혈액형 갯수를 파악하였고
# 딕셔너리로 리턴하였다. def의 bloodType은 그냥 입력받은 함수이고 리스트의bloodType과는 다르다.