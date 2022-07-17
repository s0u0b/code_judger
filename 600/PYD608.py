nums = []
for _ in range(9):
    nums.append(int(input()))
max_num = max(nums)
max_num_index = nums.index(max_num)
min_num = min(nums)
min_num_index = nums.index(min_num)


def matrix_index(index):
    return f'({index // 3}, {index % 3})'


print(f"""
Index of the largest number {max_num} is: {matrix_index(max_num_index)}
Index of the smallest number {min_num} is: {matrix_index(min_num_index)}
""")
