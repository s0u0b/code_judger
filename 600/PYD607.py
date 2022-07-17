def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])


student = [[], [], []]
for num in range(3):
    print(f'The {ordinal(num + 1)} student:')
    for _ in range(5):
        student[num].append(int(input()))
for num in range(3):
    print(f'''Student {num+1}
#Sum {sum(student[num])}
#Average {sum(student[num]) / 5:.2f}''')
