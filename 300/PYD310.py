num = int(input())
s = 0
for i in range(1, num):
    s += 1 / (i ** 0.5 + (i + 1) ** 0.5)
print(f'{s:.4f}')
