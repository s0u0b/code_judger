num1 = int(input())
num2 = int(input())

sum_ = 0
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        sum_ += i
print(sum_)
