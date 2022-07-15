num1 = int(input())
num2 = int(input())
operator = input()

if '+' in operator:
    print(num1 + num2)
elif '-' in operator:
    print(num1 - num2)
elif '*' in operator:
    print(num1 * num2)
elif '//' in operator:
    print(num1 // num2)
elif '/' in operator:
    print(num1 / num2)
elif '%' in operator:
    print(num1 % num2)
