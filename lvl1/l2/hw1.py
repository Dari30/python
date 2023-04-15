# Increased complexity: Add to the program the input of the lengths of the sides of the triangle and calculate the area according to the formula: "S = √ (p * (p - a)*(p - b)*(p - c))", where "S" is the area of the triangle, "p" is the semi perimeter of the triangle, "a,b,c" from "p=(a+b+c)/2" are the lengths of the sides of the triangle. Use the "math.sqrt" from the "math" library to calculate the square root.
length1 = int(input("What length of the side1 of the triangle"))
length2 = int(input("What length of the side2 of the triangle"))
length3 = int(input("What length of the side3 of the triangle"))
p = (length1+length2+length3)/2
import math
print( f"Ttriangle area is, {math.sqrt(p * (p - length1)*(p - length2)*(p - length3-0))}")