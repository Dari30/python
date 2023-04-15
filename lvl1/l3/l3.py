age=18
# > < >= <= == !=
if 7 <= age <= 17:
  print("You go to school")

if 5 == "5":
  print("If you see this line, then the impossible has happened")

things = "A notebook and a pencil are on the table"
if "notebook" in things:
  print ("I found a notebook")
if "pen" not in things:
  print ("I couldn't find a pen")

temp = int(input("What is the current temperature?"))
if -12<=temp <= 0:
  print("Very cold")
elif 0 < temp <= 12:
  print("Cold")
elif 12 < temp <= 18:
  print("Cool")
else:
  print("I don't know :(")

money = True
seats = True
if money == True and seats == True:
  print("You can buy a movie ticket")

age = 13
parents = True
if age >= 12 or parents == True:
  print("You can watch a movie")