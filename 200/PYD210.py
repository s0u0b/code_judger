side1 = eval(input())
side2 = eval(input())
side3 = eval(input())
check1 = (side1+side2) > side3
check2 = (side2+side3) > side1
check3 = (side3+side1) > side2

if check3 and check2 and check1:
    print(side1+side2+side3)
else:
    print('Invalid')
