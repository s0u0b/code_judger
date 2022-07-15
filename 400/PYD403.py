a = int(input())
b = int(input())
print_count = 0
print_sum = 0
for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        print(f'{i:<4}', end='')
        print_count += 1
        print_sum += i
        if print_count % 10 == 0 and i < b + 1:
            print()
print()
print(print_count)
print(print_sum)
