def compute(x, y):
    if y > x:
        x, y = y, x
    while True:
        x, y = y, x % y
        if y == 0:
            break
    return x


x_, y_ = map(int, input().split(','))
m_, n_ = map(int, input().split(','))

p = x_ * n_ + m_ * y_
q = y_ * n_
r = compute(p, q)

print(f'{x_}/{y_} + {m_}/{n_} = {p // r}/{q // r}')
