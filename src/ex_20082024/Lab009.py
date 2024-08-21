# Equilateral triagle>>>all the sides are equal
# isoseles triangle>>>>only two sides are equal
# scalane triangle>>>>none of the sides are not equal

# Program to clasify a triangle based on sides::given three input values::determine if the triangle is equilateral or
# isoseles or scalane using if else statement
side1 = int(input("enter the value of side 1 of a triangle :"))
side2 = int(input("enter the value of side 2 of a triangle :"))
side3 = int(input("enter the value of side 3 of a triangle :"))
if side1 == side2 == side3:
    print("The given sides of the triangle is equilateral")
elif side1 == side2 and side2 != side3:
    print("The given sides of a triangle is isoceles")
else:
    print("The given sides of a triangle is scalene")
