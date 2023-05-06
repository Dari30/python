# one=1
# while one<10:
#     print(f"cong{one}")
#     one+=3
# c=0
# while c<10:
#     c+=1
#     if c%2==0:
#         continue
#     print(c)
# while True:
#     print("This is endless loop")
#     ans = input("Do you want to stop the loop?y/n")
#     if ans =="y":
#         break

# word = "banana"
# for l in word:
#     print(l, end=" ")
# for i in range(8):
#     print(i)
# for i in range(3,9):
#     print(i)
# for i in range(12,9,-1):
#     print(i)

money = int(input("How much money do you have? "))
per_day = int(input("How much money do you want to save per day? "))
# days = int(input("How many days are you going to do this? "))
# print(f"You will have {money+per_day*days}")
goal = int(input("What is you goal? "))
# print(f"You will achieve your goal in {(goal-money)/per_day} days")
days=0
while money<goal:
    money+=per_day
    days+=1
print(f"You will achieve your goal in {days} days")
