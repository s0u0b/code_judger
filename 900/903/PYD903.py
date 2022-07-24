file = open("data.txt", 'a+')
print(file=file)
for i in range(5):
    print(input(), file=file)
print("Append completed!")
print('Content of "data.txt":')
file.seek(0)
print(file.read(), end='')
file.close()
