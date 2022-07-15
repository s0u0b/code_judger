import math

radius = eval(input())
perimeter = radius*2*math.pi
area = radius**2*math.pi

print(f"""Radius = {radius:.2f}
Perimeter = {perimeter:.2f}
Area = {area:.2f}""")
