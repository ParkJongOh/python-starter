# 클래스를 생성 할 때 괄호안에 인자값을 넘겨주면 __init__ 이 받는다
# 게임으로 따지면 기본스텟 정보는 속성이고 동작행동은 메소드다


class sword:
    def __init__(self, eventItem = ""):
        self.hp = 200
        self.mp = 100
        self.attack = 20
        self.defence = 20
        self.inventory = eventItem
        self.skillLevel = 1
    def slash(self):
        if self.skillLevel == 1:
            print("베기!!!")
        elif self.skillLevel == 2:
            print("두번베기!!")
    def drinkpotion(self):
        self.hp += 50
        if self.hp > 200:
            self.hp = 200

char1 = sword()
char1.inventory = "아이템"
char1.hp = 160
char1.drinkpotion()
print(char1.attack)
