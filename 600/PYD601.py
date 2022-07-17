nums = []
for _ in range(12):
    nums.append(int(input()))
even_sum = 0
for i, num in enumerate(nums,start=1):
    print(f'{num:>3}', end='')
    if i % 3 == 0:
        print()
    if (i-1) % 2 ==0:
        even_sum += num
print(even_sum)
