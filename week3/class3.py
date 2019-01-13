# 저그라는 클래스가 있고
# 저그의 기본값은 미네랄(M), 가스(G) 는 처음에 0 이다
# getM() 메소드는 미네랄을 5씩 증가시켜주고 getG() 메소드는 가스를 3씩 증가시켜준다
# makeDron() 메소드는 "드론이 생성되었습니다"라는 메세지와 함께 미네랄 3, 가스가 1씩 줄어들어요
# 만약 미네랄과 가스가 둘중에하나라도 없다면 "미네랄 또는 가스가 부족합니다" 라고 출력해줍니다

class zerg:
    def __init__(self):
        self.M = 0
        self.G = 0

    def getM(self):
        self.M += 5
    def getG(self):
        self.G += 3
    def makeDron(self):
        if self.M < 3 and self.G < 1:
            print("미네랄 또는 가스가 부족합니다.")
        else:
            self.M -= 3
            self.G -= 1
            print ("드론이 생성되었습니다.")




zerg1 = zerg()
zerg1.getM()
zerg1.getM()
zerg1.getG()
zerg1.makeDron()
zerg1.makeDron()
zerg1.makeDron()
zerg1.makeDron()
zerg1.makeDron()
