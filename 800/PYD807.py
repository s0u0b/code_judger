total = 0
nums = input()
nums = nums.split()
for num in nums:
    total += eval(num)

print(f"""Total = {total}
Average = {total / 5:.1f}""")
