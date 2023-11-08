import random


class Insect:

    # 1. set the insect attributes (name, food, feeling of fullness)
    def __init__(self, name, food, feeling):
        self.name = name
        self.food = food
        self.feeling = feeling


    # 2. increase/decrease the desired attributes
    def eat(self):
        self.feeling += 1
        self.food -= 1
        print("bee ate . food-=1", "feeling has been increased. feeling+=1")
        pass

    # 3. after searching for food, increase/decrease the desired attributes
    def find_food(self):
        f = random.randint(0, 3)
        self.food+=f
        if f>=1:
            print(f" find food, food+={f}. feeling-=1")
        else:
            print("hasn't found food. feeling -= 1")
        self.feeling -= 1



# 4. inherit the class of bee from the class of insects
class Bee(Insect):
    # 5. set the attributes of the bee (the amount of honey, in addition to other attributes)
    def __init__(self, name, food, feeling, honey):
        super().__init__(name, food, feeling)
        self.honey = honey
        pass

    # 6. after collecting honey increase/decrease the desired attributes
    def collecting_honey(self):
        self.feeling += 1
        self.honey += 1
        print("honey has been collected. honney+=1", "feeling has been increased. feeling+=1")
        pass

    # 7. this method is ready, you will need to run it at the very last moment and explain how it works
    def live(self):

        if self.feeling <= 0:
            print(f'{self.name} died :(')
            return False
        action = random.randint(1, 3)
        if self.feeling < 4:
            if self.food == 0:
                self.find_food()
            else:
                self.eat()
        else:
            if action == 1:
                self.collecting_honey()
            elif action == 2:
                self.eat()
            else:
                self.find_food()
        return True


# 8. the bee lives 30 days (if it dies, iterations end)
bee=Bee("bee",5,10,6)
for day in range(1,31):
    print(f"it is a {day}, day")
    r=bee.live()
    if r==False:
        break
