def compute(x, y):
    if y > x:
        x, y = y, x
    while True:
        x, y = y, x % y
        if y == 0:
            break
    return x


x_, y_ = input().split(',')
print(compute(int(x_), int(y_)))
