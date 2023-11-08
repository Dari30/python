class Car:
    speed = 100
    color = "black"

    def beep(self):
        print("beep")

    def p_color(self):
        print(self.color)

    def __init__(self, speed, color):
        self.color = color
        self.speed = speed


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("hello i am " + self.name)


class Student(Person):
    def __init__(self, school, grade, name, age):
        super().__init__(name, age)
        self.school = school
        self.grade = grade


class Transport:
    def __init__(self, speed, color):
        self.color = color
        self.speed = speed

    def move(self, distance):
        print("transport has move by " + distance)

    def beep(self):
        print("beep")


class Bus(Transport):
    def __init__(self, speed, color, seats):
        super().__init__(speed, color)
        self.seats = seats

    def move(self, distance):
        print("Bus has moved by " + distance)


car = Car(10, "green")
car.beep()
car1 = Car(50, "red")
car1.color = "red"
car.p_color()
print(car1.color)
person = Person("marry", 88)
person.introduce()
bus = Bus(40, "pink", 5)
student = Student("Harvard", 11, "sas", 15)
