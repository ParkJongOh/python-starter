# 예외처리는 오류를 잡기위한 용도로 사용한다
# 실제로직은 try안에다 정의하고
# 오류가 발생했을때 로직을 except안에다가 정의를 한다
# 예외처리는 알고만가자
# 사실 예외처리보다 밸류데이션 체크라는것을 많이한다
# 특정 에러에대해서 잡고싶으면 except 옆에 에러명을 입력해준다
# https://docs.python.org/3/library/exceptions.html
# finally는 성공에러여부와 상관없이 실행시키고싶은 로직을 정의한다

try:
    number = int(input())
except ValueError:
    print("정수만 입력해주세요")
except ZeroDivisionError:
    print("정수만 입력해주세요")
finally:
   a.close()

# def vaildCheck(number):
#         if type(number) != int:
#             print("정수형만 입력해주세요.")
#
# number = input()
# vaildCheck(number)
