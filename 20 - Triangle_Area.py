''' Take three sides of a triangle, and then calculate the area of the triangle '''


import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) # Triangle area formula

    return area

side_a = float(input("Input side A value: \n"))
side_b = float(input("Input side B value: \n"))
side_c = float(input("Input side C value: \n"))

print("The area of your triangle is : ", triangle_area(side_a, side_b, side_c))
