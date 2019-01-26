class sword:
    def __init__(self):
        self.attack = 110
        self.hp = 800
        self.mp = 560
        self.skillLv = 1
        self.exp = 0
        self.M = 0
    def drinkposition(self):
        if self.hp >= 800:
            print("더이상 체력을 채울 수 없습니다.")
        else:
            self.hp + 60
        if self.hp > 800:
            self.hp = 800
    def expBar(self):

class monster:


sword1 = sword()

sword1.hp = 850
sword1.drinkposition()
print(sword1.hp)

