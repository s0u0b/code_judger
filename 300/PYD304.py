num = int(input())

sum_ = 0
for i in range(num + 1):
    if i % 5 == 0:
        sum_ += i

print(sum_)
