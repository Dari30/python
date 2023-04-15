# fruits = ["apple","banana"]
# print(fruits)
# fruits.append("orange")
# print(fruits)
# if "apple" in fruits:
#     print("There is apple")
# if "z" not in "apple":
#     print("There is no z in apple")
# word = "waffles"
# attempts = 7
# letters = []
# while attempts > 0:
#     letter = input("Enter a letter ")
#     letters.append(letter)
#     won=True
#     for l in word:
#         if l in letters:
#             print(l, end=" ")
#         else:
#             print("*", end=" ")
#             won=False
#     print()
#     if letter not in word:
#         attempts -= 1
#         print("letter not in the word")
#     if won:
#         print("You won")
#         break
#     if attempts==0:
#         print("You lost")