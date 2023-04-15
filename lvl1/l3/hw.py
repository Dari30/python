month = int(input("Enter a number of the month "))
if 1 <= month <= 2:
    print("winter month")
if month == 12:
    print("winter month")
if 3 <= month <= 5:
    print("spring month")
if 6 <= month <= 8:
    print("summer month")
if 9 <= month <= 11:
    print("fall month")
if 0 >= month or month >= 13:
    print("You entered an invalid number.")