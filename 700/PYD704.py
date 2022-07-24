nums = set()
while True:
    num = eval(input())
    if num == -9999:
        break
    nums.add(num)


print(f"""Length: {len(nums)}
Max: {max(nums)}
Min: {min(nums)}
Sum: {sum(nums)}""")
