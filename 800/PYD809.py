password = input()
is_len_bigger_then_8 = len(password) >= 8
is_all_digit_and_alpha = True
is_has_upper = False
for char in password:
    if not char.isdigit() and not char.isalpha():
        is_all_digit_and_alpha = False
    if char.isupper():
        is_has_upper = True
if is_len_bigger_then_8 and is_all_digit_and_alpha and is_has_upper:
    print('Valid password')
else:
    print('Invalid password')
