even_count = odd_count = 0
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f'Even numbers: {even_count}')
print(f'Odd numbers: {odd_count}')
