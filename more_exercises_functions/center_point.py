from math import floor
def center_point(x1, x2, y1, y2):
    point1 = abs(x1) + abs(x2)
    point2 = abs(y1) + abs(y2)
    result = f"({floor(x1)}, {floor(x2)})"
    if point2 < point1:
        result = f"({floor(y1)}, {floor(y2)})"
    return result

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

print(center_point(num1, num2, num3, num4))