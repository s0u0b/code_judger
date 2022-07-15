num = int(input())
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f'{j:<2}{"*":<2}{i:<2}{"=":<2}{j * i:<4}', end='')
    print()
