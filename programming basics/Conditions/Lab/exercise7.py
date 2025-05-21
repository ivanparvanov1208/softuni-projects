from math import pi

typeOfFigure = input("Enter the type of the figure (square, rectangle, circle, triangle)\n")

if typeOfFigure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

elif typeOfFigure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
    print(f"{area:.3f}")

elif typeOfFigure == "circle":
    radius = float(input())
    area = pi * radius ** 2
    print(f"{area:.3f}")

elif typeOfFigure == "triangle":
    sideA = float(input())
    heightA = float(input())
    area = (sideA * heightA) / 2
    print(f"{area:.3f}")