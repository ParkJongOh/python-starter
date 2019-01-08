def oddEven(number):
    if number % 2 == 0:
        print("짝수입니다.")
    elif number % 2 != 0:
        print("홀수입니다.")

number = int(input())
oddEven(number)

# 1. 홀수짝수를 체크 하는 함수를 만들어라