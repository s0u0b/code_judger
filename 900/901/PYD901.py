with open("write.txt", 'w') as f:
    for index in range(5):
        print(input(), file=f)
