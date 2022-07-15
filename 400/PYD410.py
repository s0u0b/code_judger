high = int(input())
for h in range(1, high + 1):
    print(' ' * (high - h) + '*' * (h*2-1))
