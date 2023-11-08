import random

class Enemy:
    def __init__(self, hp , damage):
        self.hp=hp
        self.damage=damage
        self.ohp = hp
    def be_attacked(self, damage):
        self.hp-=damage
    def heal(self):
        self.hp+=self.ohp*0.6
        if self.hp > self.ohp:
            self.hp=self.ohp
enemies=[Enemy(10,100),Enemy(20,50),Enemy(40,25)]
enemy1=random.choice(enemies)
enemies.remove(enemy1)
enemy2=random.choice(enemies)
while True:
    print(enemy1.hp)
    print(enemy2.hp)
    enemy1.be_attacked(enemy2.damage)
    onee=int(input("choose from \n 1:attack\n 2:heal\n:"))
    if onee==1:
        enemy2.be_attacked(enemy1.damage)
    if onee==2:
        enemy1.heal()
    if enemy1.hp <=0 and enemy2.hp <=0:
        print("both died")
        break
    if enemy1.hp <=0:
        print("enemy1 died")
        break
    if enemy2.hp <=0:
        print("enemy2 died")
        break