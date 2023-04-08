import random
# # print("Hello, guest")
# # print(5+5)
# # print("Hello "+"player")
# # name = input("what is your name")
# # age = float(input("how old are you"))
# # print (name, "you've lived",age*365*24*60*60,"seconds")
print("Hello, user "+"try to guess a number form 1 to 10")
number = random.randint(1,10)
user_number = int(input("enter a number: "))
if number<user_number:
    print("my number is less")
if number>user_number:
    print("my number is greater")
if number==user_number:
    print("congratulations you have guessed the number")
attempts = 3
while attempts>0:
    print("attempts left:"+str(attempts))
    user_number = int(input("enter a number: "))
    if number<user_number:
        print("my number is less")
        attempts-=1
    if number>user_number:
        print("my number is greater")
        attempts-=1
    if number==user_number:
        print("congratulations you have guessed the number")
        break
# length = float(input("Hi, What is square length"))
# print ("Your square area is, ", length*length, "m2")
# length = float(input("Hi, What is square length"))
# print ("Your square perimeter is, ", length*4, "m")
# length = float(input("Hi, What is rectangle length"))
# width = float(input("Hi, What is rectangle width"))
# print ("Your square area is, ", length*width, "m2")
# length = float(input("Hi, What is rectangle length"))
# width = float(input("Hi, What is rectangle width"))
# print ("Your rectangle perimeter is, ", (length+width)*2, "m")
# age = int(input("How old are you"))
# number = 18
# if number>age:
#     print("You are under 18")
# if number<age:
#     print("You are over 18")