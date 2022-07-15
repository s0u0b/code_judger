def compute(a, b):
    continued_addition = 0
    for i in range(a, b + 1):
        continued_addition += i
    print(continued_addition)


a_ = int(input())
b_ = int(input())
compute(a_, b_)
