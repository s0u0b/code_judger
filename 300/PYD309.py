money = int(input())
rate = eval(input())
month = int(input())
print('%s \t  %s' % ('Month', 'Amount'))
for i in range(1, month + 1):
    total = money + money * rate / 1200
    money = total
    print('%3d \t %.2f' % (i, total))
