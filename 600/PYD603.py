nums = []
for _ in range(10):
    nums.append(int(input()))
nums.sort(reverse=True)
print(f'{nums[0]} {nums[1]} {nums[2]}')
