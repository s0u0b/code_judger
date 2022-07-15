str_ = input()
if str_.isdigit():
    print(f'{str_} is a number.')
elif str_.isalpha():
    print(f'{str_} is an alphabet.')
else:
    print(f'{str_} is a symbol.')