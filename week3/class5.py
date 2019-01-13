# common이라는 클래스에는
# 메소드 qKey(), wKey(), ekey(), rKey()
# 메소드가 실행되면 "q공격이 실행되었습니다"
# 속성값 hp, mp, ep 라는값이 기본값으로 200,100,100으로 설정되어있다

# vladmir 클래스는
# common이라는 클래스를 상속받아서
# 속성값에는 type

class common:
    def __init__(self):
        self.hp = 200
        self.mp = 100
        self.ep = 100

    def qKey(self):
        print("q공격이 실행되었습니다.")
    def wKey(self):
        print("w공격이 실행되었습니다.")
    def eKey(self):
        print("e공격이 실행되었습니다.")
    def rKey(self):
        print("r공격이 실행되었습니다.")

class vladmir(common):
    def rKey(self):
        print("피를 빨았습니다.")


vlad = vladmir()

vlad.rKey()
vlad.qKey()
