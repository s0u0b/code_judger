nums = []
while True:
    num = eval(input())
    if num == -9999:
        break
    nums.append(num)

print(f"""{tuple(nums)}
Length: {len(nums)}
Max: {max(nums)}
Min: {min(nums)}
Sum: {sum(nums)}""")
