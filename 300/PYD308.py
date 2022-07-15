count_of_num = int(input())
for _ in range(count_of_num):
    num = input()
    sum_ = 0
    for n in num:
        sum_ += int(n)
    print(f'Sum of all digits of {num} is {sum_}')