import math
n = eval(input())
s = eval(input())

print(f'Area = {(n*math.pow(s,2))/(4*math.tan(math.pi/n)):.4f}')
