class Player:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def showstats(self):
        print("HP " + str(self.hp) + " Attack " + str(self.attack))

    def takeDamage(self, dmg):
        self.hp -= dmg
        print("Player took " + str(dmg) + " damage!")
        print("Current HP: " + str(self.hp))

p = Player(10, 3, 2)
p.takeDamage(3)
p.showstats()

