num = int(input())

for i in range(1, num + 1):
    for j in range(1, i+1):
        print(f'{i * j:>4}', end='')
    print()
