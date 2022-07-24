print("Create tuple1:")
nums1 = []
while True:
    num = eval(input())
    if num == -9999:
        break
    nums1.append(num)

print("Create tuple2:")
nums2 = []
while True:
    num = eval(input())
    if num == -9999:
        break
    nums2.append(num)

combined_nums = nums1 + nums2
print(f"""Combined tuple before sorting: {tuple(combined_nums)}
Combined list after sorting: {sorted(combined_nums)}
""")
