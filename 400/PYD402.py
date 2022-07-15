input_num = eval(input())
min_ = input_num
while input_num != 9999:
    min_ = min(min_, input_num)
    input_num = eval(input())
print(min_)