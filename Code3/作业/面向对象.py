# _*_ coding:utf-8 _*-
# 一、请写一个小游戏，人狗大战，2个角色，人和狗，游戏开始后，生成2个人，3条狗，互相混战，
# 人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。

class Aniamal:
    def __init__(self, hp1, attack):
        self.hp1 = hp1  # 实例属性：实例对象自己私有。---》self.name   self.classname
        self.attack = attack
class people(Aniamal):
    count = 2

    def __init__(self, hp1, attack, num):
        super().__init__(hp1, attack)
        self.num = num

    def beat(self):
        self.hp1 = self.hp1 - 20
        self.attack = self.attack - 1
        if self.hp1 <= 0:
            print("人死了!!")
        return self.hp1
class dog(people):
    count = 3

    def __init__(self, hp1,hp2, attack, num):
        super().__init__(hp1,attack,num)
        self.hp2 = hp2

    def bite(self):
        self.hp2 = self.hp2 - 15
        self.attack = self.attack - 2
        if self.hp2 <= 0:
            print("狗死了!!")
        elif self.hp2 <= self.hp1:
            print("狗输了！！")
        elif self.hp2 > self.hp1:
            print("狗赢了！！")
        else:
            print("不是个东西！！")


a = people(120 * people.count, 10, 2)
b = dog(120 * people.count,100 * dog.count, 50, 3)
print("开始决斗")
for i in range(1, 11):
    a.beat()
    b.bite()

print("人的血量为{0}".format(a.hp1))
print("人的攻击力为{0}".format(a.attack))
print("狗的血量为{0}".format(b.hp2))
print("狗的攻击力为{0}".format(b.attack))
