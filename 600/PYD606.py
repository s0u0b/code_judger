def compute(row, col):
    for r in range(row):
        for c in range(col):
            print(f'{c - r:>4}', end='')
        if r - 1 != row:
            print()


row_ = int(input())
col_ = int(input())
compute(row_, col_)
