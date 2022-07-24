string = input()
sum_of_ascii = 0
for index, c in enumerate(string):
    print(f"ASCII code for '{c}' is {ord(c)}")
    sum_of_ascii += ord(c)
print(sum_of_ascii)
