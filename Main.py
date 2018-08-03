#Parent class for player and enemies
class Char:
    def __init__(self, hp, attack, magic, defence):
        self.hp = hp
        self.attack = attack
        self.magic = magic
        self.defence = defence

    # Display stats
    def showstats(self):
        print("HP " + str(self.hp) + " Attack " + str(self.attack) + " Magic " + str(self.magic) +  " Defence " + str(self.defence))   # Enemies will override this function

    def takeDamage(self, dmg):
        self.hp -= dmg
        print("Player took " + str(dmg) + " damage!")
        print("Current HP: " + str(self.hp))

# Level = Determine max deck?
class Player(Char):
    def __init__(self, hp, attack, magic, defence, level):
        Char.__init__(self, hp, attack, magic, defence)
        self.level = level


class Enemy(Char):
    def __init__(self, hp, attack, magic, defence, level, name):
        Char.__init__(self, hp, attack, magic, defence)
        self.level = level
        self.name = name

    # Override
    def takeDamage(self, dmg):
        self.hp -= dmg
        print(self.name + " took " + str(dmg) + " damage!")
        print("Current HP: " + str(self.hp))

p = Player(10, 0, 0, 0, 1)
p.takeDamage(3)
p.showstats()

e = Enemy(5, 2, 1, 1, 1, "Slime")
e.takeDamage(2)
e.showstats()