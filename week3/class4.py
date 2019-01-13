# 상속을 받을때는 클래스명 옆에 괄호를 열어 괄호안에 상속받을 클래스명을 입력한다
# 오버라이딩은 상속받은 메소드명을 덮어씌어준다라고 이해하면 쉽다

class common():
    def __init__(self):
        self.M = 0
        self.G = 0

    def getM(self):
        self.M += 5
    def getG(self):
        self.G += 3

class zerg(common):
    def makeDron(self):
        if self.M < 3 and self.G < 1:
            print("미네랄 또는 가스가 부족합니다.")
        else:
            self.M -= 3
            self.G -= 1
            print ("드론이 생성되었습니다.")

class terran(common):
    def makeSCV(self):
        if self.M < 3 and self.G < 1:
            print("미네랄 또는 가스가 부족합니다.")
        else:
            self.M -= 3
            self.G -= 1
            print ("드론이 생성되었습니다.")

class prot(common):
    def makeProve(self):
        if self.M < 3 and self.G < 1:
            print("미네랄 또는 가스가 부족합니다.")
        else:
            self.M -= 3
            self.G -= 1
            print ("드론이 생성되었습니다.")

    def getM(self):
        self.M += 6

prot1 = prot()
prot1.getM()
prot1.getM()
prot1.getM()
print(prot1.M)