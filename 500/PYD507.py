def compute(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


num_ = int(input())
if compute(num_):
    print('Prime')
else:
    print('Not Prime')
