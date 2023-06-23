# Write a function to calculate the area of the circle. The function takes the value of the radius "r" and calculates the area by the "S=π* r*r" formula, where "S" is the area of the circle, "π = 3.14," "r" is the radius of the circle. The calculated value needs to be returned
def circle_area(r):
    s=3.14*r*r
    return s

print(circle_area(8))

r = int(input('What is the radius of circle  : '))
p = 3.14
print(f"The area of circle is {p*r*r}")

