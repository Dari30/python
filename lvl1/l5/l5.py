points = 100
while points > 0:
    user_number = int(input("Say number from 2 to 12 "))
    bet = int(input("Make the bet "))
    import random
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    sum_number = number1+number2
    if sum_number < 7 and user_number < 7:
        points+=bet
    elif sum_number > 7 and user_number > 7:
        points+=bet
    elif sum_number == user_number:
        points+=bet*4
    else:
        points-=bet
    print("Now you have",points, "points ")
    ans = input("Do you want to continue this game?y/n")
    if ans =="n":
        break
