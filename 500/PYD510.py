def compute(num):
    a, b = 0, 1
    count = 0
    while True:
        print(f'{a} ', end='')
        count += 1
        if count == num:
            break
        a, b = b, a + b


num_ = int(input())
compute(num_)
