nums = []
for _ in range(10):
    nums.append(int(input()))
nums.remove(max(nums))
nums.remove(min(nums))
num_sum = sum(nums)
num_avg = num_sum / 8

print(num_sum)
print(f'{num_avg:.2f}')
