

# Write a function that takes three numbers and returns the smallest of them.
def minimum(a,b,c):
    if a < b and a < c :
        return a
    if b < a and b < c :
        return b
    if c < a and c < b :
        return c


# a = int(input('Enter first number  : '))
# b = int(input('Enter second number : '))
# c = int(input('Enter third number  : '))
# print(snumber, "is the smallest number.")