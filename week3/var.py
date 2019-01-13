# 지역내에서만 사용 할 수 있는 변수를 지역변수
# 모든곳에서 사용 할 수 있는 변수를 전역변수

num = 1
def test():
    global num
    print(num)

test()
