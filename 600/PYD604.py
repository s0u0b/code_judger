nums = []
for _ in range(10):
    nums.append(int(input()))
nums.sort(reverse=True, key=nums.copy().count)
print(nums[0])
print(nums.count(nums[0]))
