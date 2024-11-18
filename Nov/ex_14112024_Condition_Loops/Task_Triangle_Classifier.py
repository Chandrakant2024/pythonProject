'''
Write a program that classifies a triangle based on its side lengths. Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal). Use an if-else statement to classify the triangle.

equilateral : all sides equal

Isosceles : 2 sides are equal

Scalene : all are diff
'''
s1=int(input("Enter first side\n"))
s2=int(input("Enter second side\n"))
s3=int(input("Enter third side\n"))

if (s1==s2 and s1==s3):
    print("It's an Equilateral triangle")
elif (s1==s2 or s1==s3 or s2==s3):
    print("It's an Isosceles triangle")
else:
    print("It's a Scalene triangle")