def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(f'{a} ', end='')
        print()


a_ = input()
x_ = int(input())
y_ = int(input())
compute(a_, x_, y_)
