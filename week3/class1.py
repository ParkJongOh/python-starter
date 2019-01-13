# 클래스를 정의 할때는 class 라고 입력하여 정의한다
# class 클래스명:
# 클래스 안에 있는 함수는 메소드라고 부른다
# 클래스를 생성하게되면 __init__이 처음에 실행 된다.
# self는 생성한 본인
# 메소드의 인자값 첫번째는 self이다. 넘겨주는값은 두번째부터

class cal:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result + num

    def c(self):
        self.result = 0

cal1 = cal()
print(cal1.result)
cal1.add(2)
cal1.add(4)
print(cal1.result)

cal2 = cal()
print(cal2.result)